from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up the HuggingFace endpoint
llm = HuggingFaceEndpoint(
    repo_id="nilq/mistral-1L-tiny",
    task="text-generation"
)

# Wrap with LangChain Chat model
model = ChatHuggingFace(llm=llm)

# Invoke the model
result = model.invoke("What is the capital of India?")
print(result.content)
