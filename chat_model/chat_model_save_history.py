# Example Source: https://python.langchain.com/v0.2/docs/integrations/memory/google_firestore/

from dotenv import load_dotenv
import os
import uuid
from datetime import datetime
from typing import List, Dict, Any, Optional

from langchain_core.messages import (
    AIMessage,
    BaseMessage,
    HumanMessage,
    SystemMessage,
)
from langchain_openai import ChatOpenAI
from supabase import create_client, Client

"""
Steps to replicate this example:
1. Create a Supabase account at https://supabase.com/
2. Create a new Supabase project
3. Get your Supabase URL and API Key from the project settings
4. Add them to your .env file as SUPABASE_URL and SUPABASE_KEY
5. Create a table in Supabase with the following SQL:

CREATE TABLE chat_messages (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    session_id TEXT NOT NULL,
    message_type TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_chat_messages_session_id ON chat_messages(session_id);

6. pip install supabase
"""

load_dotenv()

# Supabase configuration
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SESSION_ID = "user_session_new"  # This could be a username or a unique ID
TABLE_NAME = "chat_messages"

# Initialize Supabase Client
print("Initializing Supabase Client...")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

class SupabaseChatMessageHistory:
    """Chat message history stored in Supabase."""

    def __init__(
        self,
        session_id: str,
        table_name: str,
        supabase_client: Client,
    ):
        """Initialize with Supabase client and session ID.

        Args:
            session_id: Unique identifier for the conversation session.
            table_name: Name of the Supabase table to store messages.
            supabase_client: Supabase client.
        """
        self.session_id = session_id
        self.table_name = table_name
        self.client = supabase_client

    @property
    def messages(self) -> List[BaseMessage]:
        """Retrieve messages from Supabase"""
        response = (
            self.client
            .table(self.table_name)
            .select("*")
            .eq("session_id", self.session_id)
            .order("created_at", desc=False)
            .execute()
        )
        
        items = response.data
        messages = []
        
        for item in items:
            if item["message_type"] == "human":
                messages.append(HumanMessage(content=item["content"]))
            elif item["message_type"] == "ai":
                messages.append(AIMessage(content=item["content"]))
            elif item["message_type"] == "system":
                messages.append(SystemMessage(content=item["content"]))
        
        return messages

    def add_message(self, message: BaseMessage) -> None:
        """Add a message to the Supabase table"""
        message_type = self._get_message_type(message)
        
        self.client.table(self.table_name).insert({
            "session_id": self.session_id,
            "message_type": message_type,
            "content": message.content,
        }).execute()

    def add_user_message(self, message: str) -> None:
        """Add a user message to the store"""
        self.add_message(HumanMessage(content=message))

    def add_ai_message(self, message: str) -> None:
        """Add an AI message to the store"""
        self.add_message(AIMessage(content=message))

    def clear(self) -> None:
        """Clear session memory from Supabase"""
        self.client.table(self.table_name).delete().eq("session_id", self.session_id).execute()

    def _get_message_type(self, message: BaseMessage) -> str:
        """Get message type from a BaseMessage."""
        if isinstance(message, HumanMessage):
            return "human"
        elif isinstance(message, AIMessage):
            return "ai"
        elif isinstance(message, SystemMessage):
            return "system"
        else:
            raise ValueError(f"Unknown message type: {type(message)}")


# Initialize Supabase Chat Message History
print("Initializing Supabase Chat Message History...")
chat_history = SupabaseChatMessageHistory(
    session_id=SESSION_ID,
    table_name=TABLE_NAME,
    supabase_client=supabase,
)
print("Chat History Initialized.")
print("Current Chat History:", chat_history.messages)

# Initialize Chat Model
model = ChatOpenAI()

print("Start chatting with the AI. Type 'exit' to quit.")

while True:
    human_input = input("User: ")
    if human_input.lower() == "exit":
        break

    chat_history.add_user_message(human_input)

    ai_response = model.invoke(chat_history.messages)
    chat_history.add_ai_message(ai_response.content)

    print(f"AI: {ai_response.content}")