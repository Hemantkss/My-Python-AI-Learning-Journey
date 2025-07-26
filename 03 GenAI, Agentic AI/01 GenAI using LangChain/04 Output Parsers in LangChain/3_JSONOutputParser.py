from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

# model = ChatHuggingFace(llm=llm)

model = ChatOpenAI()

# Parser 
parser = JsonOutputParser()

# Template 
temaplate = PromptTemplate(
    template="Give me the names, of cities in {format_instructions}",
    input_variables=[],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

chain = temaplate | model | parser

result = chain.invoke({'format_instructions': 'json'})

print(result)