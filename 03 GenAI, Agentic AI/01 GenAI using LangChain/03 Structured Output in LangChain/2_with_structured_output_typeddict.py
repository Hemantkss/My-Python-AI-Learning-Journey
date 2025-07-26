from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatOpenAI()

# Schema
class Review(TypedDict):
    summary: str
    sentiment: str
    
structured_output = model.with_structured_output(Review)

result = structured_output.invoke(
    """
    TypedDict is a feature in Python that lets you define what keys and value types a dictionary should have.
    Use TypedDict when you want a lightweight way to make your code safer and easier to read without using classes or external libraries.
    """
)

print(result)
print(result['summary'])
print(result['sentiment'])