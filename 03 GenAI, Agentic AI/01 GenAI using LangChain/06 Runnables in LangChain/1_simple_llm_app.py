from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()
model = ChatOpenAI()

prompt = PromptTemplate(
    template="Suggest a catchy blog title about {topic}",
    input_variables=["topic"]
)

topic = input("Enter a topic: ")

formatted_prompt = prompt.format(topic=topic)

blog_title = model.predict(formatted_prompt)

print("Blog title:", blog_title)