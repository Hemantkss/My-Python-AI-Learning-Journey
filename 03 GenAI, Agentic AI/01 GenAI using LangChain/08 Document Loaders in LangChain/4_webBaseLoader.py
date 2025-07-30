
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize LLM
model = ChatOpenAI()

# Create prompt template
prompt = PromptTemplate(
    template='Answer the following question:\n{question}\n\nBased on the following text:\n{text}',
    input_variables=['question', 'text']
)

# Parser for output
parser = StrOutputParser()

# Flipkart product URL
url = 'https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7x4hn-a/p/itmdc5308fa78421'

# Load web content
loader = WebBaseLoader(url)
docs = list(loader.lazy_load())  # Convert generator to list

# Chain prompt → model → parser
chain = prompt | model | parser

# Ask question using loaded content
response = chain.invoke({
    'question': 'What is the product that we are talking about?',
    'text': docs[0].page_content
})

print("Answer:\n", response)
