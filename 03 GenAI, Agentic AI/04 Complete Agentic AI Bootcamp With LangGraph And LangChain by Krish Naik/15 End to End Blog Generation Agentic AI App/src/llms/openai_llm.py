from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

class OpenAI_LLM:
    def __init__(self):
        load_dotenv()
        
        
    def get_llm(self):
        try:
            os.environ["OPENAI_API_KEY"] = self.openai_api_key = os.getenv("OPENAI_API_KEY")
            llm = ChatOpenAI(model="gpt-4o")
            return llm
        
        except Exception as e:
            raise ValueError(f"Error initializing OpenAI LLM:  {e}")

