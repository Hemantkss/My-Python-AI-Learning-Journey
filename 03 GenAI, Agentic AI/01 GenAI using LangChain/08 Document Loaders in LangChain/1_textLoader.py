from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

loader = TextLoader('cricket.txt', encoding='utf-8')
docs= loader.load()
# print(type(docs))
# print(len(docs))
# print(docs[0].page_content)
# print(docs[0].metadata)

prompt = PromptTemplate(
    template="Summarize this poem: {text}",
    input_variables=["text"]
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"Poem", docs[0].page_content})

print(result)