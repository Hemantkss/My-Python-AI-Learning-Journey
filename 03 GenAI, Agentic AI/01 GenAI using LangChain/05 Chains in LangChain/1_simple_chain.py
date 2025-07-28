from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate # type: ignore
from langchain_core.output_parsers import StrOutputParser # pyright: ignore[reportMissingImports]

load_dotenv()

prompt = PromptTemplate(
    template="Generate a 5 instresting facts about {topic}",
    input_variables=["topic"],
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"topic": "human"})

print(result)

chain.get_graph().print_ascii()