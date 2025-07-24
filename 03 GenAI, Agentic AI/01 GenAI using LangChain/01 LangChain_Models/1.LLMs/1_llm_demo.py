# ✅ Import the necessary module to load environment variables from a .env file
from dotenv import load_dotenv

# ✅ Import the OpenAI LLM wrapper from LangChain's OpenAI integration
from langchain_openai import OpenAI

# ✅ Load environment variables from the .env file
# This includes your OpenAI API key (make sure OPENAI_API_KEY is set in your .env)
load_dotenv()

# ✅ Create an LLM instance using OpenAI's "gpt-3.5-turbo-instruct" model
# This model supports instruction-following like GPT-3.5 with text input/output
llm = OpenAI(model='gpt-3.5-turbo-instruct')

# ✅ Call the model using the `invoke()` method
# This sends the input prompt to the model and receives the generated response
result = llm.invoke("Hello, What is capital of India?")

# ✅ Print the model's output (should be "The capital of India is New Delhi.")
print(result)
