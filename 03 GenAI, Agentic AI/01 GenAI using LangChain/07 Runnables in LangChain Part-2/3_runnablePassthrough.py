from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()
model = ChatOpenAI()

# Prompt 1
prompt1 = PromptTemplate(
    template="Gerate a joke about {topic}",
    input_variables=["topic"]
)

# Prompt 2
prompt2 = PromptTemplate(
    template="Explain the following joke - {text}",
    input_variables=['text']
)

parser = StrOutputParser()

joke_genarator_chain = RunnableSequence(prompt1, model, parser)

runnable_parallel = RunnableParallel({
    "joke": RunnablePassthrough(),
    "explain": RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(joke_genarator_chain, runnable_parallel)

result = final_chain.invoke({"topic": "cars"})

# print(result)

print("Joke: ", result["joke"])
print("Explanation: ", result["explain"])

