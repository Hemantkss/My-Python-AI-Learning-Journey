from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

# 1st Prompt -> detail report
tem1 = PromptTemplate(
    template='Write a Detailed report on {topic}',
    input_variables=['topic']
)


# 2nd Prompt -> summary
tem2 = PromptTemplate(
    template='Write a 5 Line Summary on {text}',
    input_variables=['text']
)

prompt1 = tem1.invoke({'topic': 'LangChain'})
result1 = model.invoke(prompt1)

prompt2 = tem2.invoke({'text': result1.content})
result2 = model.invoke(prompt2)

print(result2.content)