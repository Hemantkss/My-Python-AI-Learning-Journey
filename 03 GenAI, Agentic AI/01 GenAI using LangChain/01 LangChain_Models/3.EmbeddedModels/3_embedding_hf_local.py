from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(mode_name="sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "The capital of India is New Delhi.",
    "The capital of France is Paris.",
    "The capital of Italy is Rome."
]

result = embedding.embed_documents(documents)

print(str(result))