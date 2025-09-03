from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langserve import add_routes
import os
from dotenv import load_dotenv
load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

# Model
model = ChatOpenAI()

# PromptTemplate
generic_prompt = 'Translate the following into {language}'
prompt = ChatPromptTemplate.from_messages(
    [
        ('system', generic_prompt),
        ('human', '{text}')
    ]
)

# strOutputParser
parser = StrOutputParser()

# Chain 
chain = prompt | model | parser

# App
app = FastAPI(
    title='langChain Server',
    version='1.0',
    description='A simple API Server using LangChain runnable interfaces'
)

# App Definition
add_routes(
    app,
    chain,
    path='/chain' 
)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)