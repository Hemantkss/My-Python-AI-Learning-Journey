from langchain_openai import ChatOpenAI 
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model_name="gpt-4", temperature=1.5, max_completion_tokens=10)

result = model.invoke("Suggest me 5 indian dishes to try today")

print(result.content)


