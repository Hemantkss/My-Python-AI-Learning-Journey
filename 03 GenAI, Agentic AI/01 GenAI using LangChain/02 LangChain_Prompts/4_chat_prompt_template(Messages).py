from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {role} expert'),
    ('human', 'Expain in simple term, what is {topic}?')
])

prompt = chat_template.invoke({'role': 'AI', 'topic': 'machine learning'})

print(prompt)