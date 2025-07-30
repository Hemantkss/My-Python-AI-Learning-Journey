from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

url = 'https://www.ndtv.com/world-news/russia-kamchatka-earthquake-tsunami-live-updates-8-8-magnitude-strongest-since-1952-tsunami-warning-japan-us-russia-hawaii-8979921'
loader = WebBaseLoader(url)
docs = loader.load()

print(len(docs))