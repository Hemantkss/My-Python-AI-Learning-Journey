from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=3)


documents = [
    "The capital of India is New Delhi.",
    "The capital of France is Paris.",
    "The capital of Italy is Rome."
]

result = embedding.embed_documents(documents)

print(str(result))