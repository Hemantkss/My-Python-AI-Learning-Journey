from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


# Chat Template
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful Customer Support Agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])


# Laod Chat History
chat_history = []

with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())
    
print(chat_history)


# Create Prompt
prompt = chat_template.invoke({'chat_history': chat_history, 'query': 'Where is my Refund request?'})

print(prompt)