from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()
model = ChatOpenAI()

prompt = PromptTemplate(
    template="Suggest a catchy blog title about {topic}",
    input_variables=["topic"]
)

chain = LLMChain(llm=model, prompt=prompt)

topic = input("Enter a topic: ")
output = chain.run(topic)

print("Blog title:", output)