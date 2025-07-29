from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence

load_dotenv()

# Prompt 1
prompt1 = PromptTemplate(
    template="Write a Joke about {topic}",
    input_variables=["topic"]
)

model = ChatOpenAI()

parser = StrOutputParser()

# Prompt 2
prompt2 = PromptTemplate(
    template="Explain the following joke - {text}",
    input_variables=['text']
)

runnable_sequence = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

result = runnable_sequence.invoke({"topic": "cars"})

print(result)