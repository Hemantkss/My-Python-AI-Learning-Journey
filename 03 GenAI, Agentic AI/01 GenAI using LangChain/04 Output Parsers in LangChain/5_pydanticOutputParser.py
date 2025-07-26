from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

# Schema
class Person(BaseModel):
    name: str = Field(description="The person's name")
    age: int = Field(gt=18 ,description="The person's age")
    city: str = Field(description="The person's city")
    
# Parser 
parser = PydanticOutputParser(pydantic_object=Person)

# Template 
template = PromptTemplate(
    template="Give a person's name, age, and city from {place}. Respond only in JSON: {format_instructions}",
    input_variables=['place'],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'place': 'india'})

print(result)
print("Name: ",result.name)
print("Age: ",result.age)
print("City: ",result.city)