This is a project for learning LangChain

## Setup

```bash
python -m venv .venv
```

### Why create a virtual environment?

Creating a virtual environment using the command above is important because:

1. **Isolation**: It creates an isolated Python environment for this project, preventing package conflicts with other projects or your system Python.
2. **Dependency Management**: It allows you to install and manage project-specific dependencies without affecting other projects.
3. **Reproducibility**: It makes it easier to recreate the exact same environment on different machines.
4. **Clean Development**: It keeps your global Python installation clean and organized.

After creating the virtual environment, you'll need to activate it:

- On Windows: `.venv\Scripts\activate`
- On macOS/Linux: `source .venv/bin/activate`

## Installing Dependencies

After activating your virtual environment, install the required packages:

```bash
pip install langchain-openai
pip install python-dotenv
pip install supabase
```

### Why install langchain-openai?

The `langchain-openai` package is essential for this project because:

1. **Integration**: It provides the necessary integration between LangChain and OpenAI's models.
2. **API Access**: It allows you to interact with OpenAI's powerful language models (like GPT-3.5, GPT-4) through LangChain's abstractions.
3. **Simplified Development**: It handles the complexity of API calls, token management, and response parsing.
4. **Compatibility**: It ensures that LangChain's features work seamlessly with OpenAI's models.
5. **Advanced Features**: It enables the use of advanced features like function calling, streaming responses, and model fine-tuning within the LangChain framework.

## Environment Variables with .env File

### Creating a .env file

1. Create a file named `.env` in the root directory of your project
2. Add your API keys in the following format:

```
OPENAI_API_KEY=your_openai_api_key_here
SUPABASE_URL=your_supabase_url_here
SUPABASE_KEY=your_supabase_api_key_here
```

### How to link .env to your Python code

To use the environment variables in your Python code, you need to:

1. Install the python-dotenv package (already included in the dependencies above)
2. Load the variables in your Python file:

```python
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access your API keys
openai_api_key = os.getenv("OPENAI_API_KEY")
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

# Now you can use the api_key with LangChain
from langchain_openai import OpenAI

llm = OpenAI(api_key=openai_api_key)
# or if OPENAI_API_KEY is set, LangChain will use it automatically
# llm = OpenAI()
```

### Important Security Note

Always add `.env` to your `.gitignore` file to prevent accidentally committing your API keys to version control:

```
# .gitignore
.env
```

## Setting Up Supabase for Chat History

### Why use Supabase for chat history?

1. **Persistence**: Stores conversation history in a reliable database
2. **Scalability**: Supabase is built on PostgreSQL, providing enterprise-grade database capabilities
3. **Easy Management**: Provides a user-friendly interface for viewing and managing data
4. **Real-time Capabilities**: Supports real-time subscriptions for live updates
5. **Authentication**: Includes built-in auth if you want to associate chat histories with users

### Steps to set up Supabase

1. Create a Supabase account at [https://supabase.com](https://supabase.com)
2. Create a new Supabase project
3. In the SQL Editor, create a table for storing chat messages:

```sql
CREATE TABLE chat_messages (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    session_id TEXT NOT NULL,
    message_type TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_chat_messages_session_id ON chat_messages(session_id);
```

4. Go to Project Settings > API to get your Supabase URL and API Key
5. Add these to your `.env` file as shown above
