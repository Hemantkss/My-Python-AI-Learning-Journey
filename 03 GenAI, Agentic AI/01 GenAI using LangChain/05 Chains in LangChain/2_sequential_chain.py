from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate # type: ignore
from langchain_core.output_parsers import StrOutputParser # pyright: ignore[reportMissingImports]

load_dotenv()

prompt1 = PromptTemplate(
    template="genarate a detailed report about {topic}",
    input_variables=["topic"],
)

prompt2 = PromptTemplate(
    template="genarate a 5 instresting facts about {text}",
    input_variables=["text"]
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({"topic": "LangChain"})

print(result)

# chain.get_graph().print_ascii()