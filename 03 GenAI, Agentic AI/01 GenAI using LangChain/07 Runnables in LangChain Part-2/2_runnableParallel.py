from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel

load_dotenv()
model = ChatOpenAI()

# Prompt 1
prompt1 = PromptTemplate(
    template="Genarate a tweet about {topic}",
    input_variables=["topic"]
)

# prompt 2
prompt2 = PromptTemplate(
    template="Genarate  a Linkedin post about {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

runnable_parallel = RunnableParallel({
    "tweet": RunnableSequence(prompt1, model, parser),
    "linkedin": RunnableSequence(prompt2, model, parser)
})

result = runnable_parallel.invoke({"topic": "AI"})

# print(result)

print("Tweet", result["tweet"])
print("Linkedin", result["linkedin"])