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
2. Add your API key in the following format:

```
OPENAI_API_KEY=your_api_key_here
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

# Access your API key
api_key = os.getenv("OPENAI_API_KEY")

# Now you can use the api_key with LangChain
from langchain_openai import OpenAI

llm = OpenAI(api_key=api_key)
# or if OPENAI_API_KEY is set, LangChain will use it automatically
# llm = OpenAI()
```

### Important Security Note

Always add `.env` to your `.gitignore` file to prevent accidentally committing your API keys to version control:

```
# .gitignore
.env
```
