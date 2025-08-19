from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

os.environ['LANGSMITH_PROJECT'] = "sequential-chain"

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

model1 = ChatOpenAI(model='gpt-4o-mini', temperature=0.7)
model2 = ChatOpenAI(model='gpt-4o', temperature=0.5)

parser = StrOutputParser()

chain = prompt1 | model1 | parser | prompt2 | model2 | parser

# Configuration for LangSmith
config = {
    'run_name': 'sequential-chain',
    'tags': ['llm_app', 'report_generation', 'summarization'],
    'metadata': {
        'model 1': 'gpt-4o-mini',
        'temperature 1': 0.7,
        'model 2': 'gpt-4o',
        'temperature 2': 0.5,
        'parser': 'StrOutputParser'
    }
}

result = chain.invoke({'topic': 'AI Evaluation in world'}, config=config)

print(result)
