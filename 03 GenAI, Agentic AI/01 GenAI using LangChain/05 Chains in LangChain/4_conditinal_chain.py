from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate # type: ignore
from langchain_core.output_parsers import StrOutputParser 
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

# Model
model = ChatOpenAI()

# parser 
parser1 = StrOutputParser()

# Feedback Class
class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="The sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

# prompt 1
prompt1 = PromptTemplate(
    template="Classify the sentiment of the following text (positive or negative) \n {feedback} \n {format_instructions}",
    input_variables=["feedback"],
    partial_variables={"format_instructions": parser2.get_format_instructions()},
)

# prompt 2 
prompt2 = PromptTemplate(
    template="Write an appropriate response to this positive Feedback \n {feedback}",
    input_variables=["feedback"],
)

# prompt 3
prompt3 = PromptTemplate(
    template="Write an appropriate response to this negative Feedback \n {feedback}",
    input_variables=["feedback"],
)



# Classifier Chain
classifier_chain = prompt1 | model | parser2

# Branch Chain
branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive", prompt2 | model | parser1),
    (lambda x: x.sentiment == "negative", prompt3 | model | parser1),
    RunnableLambda(lambda x: "Invalid Feedback"),
)

# Final Chain
final_chain = classifier_chain | branch_chain

result = final_chain.invoke({"feedback": "The model is very bad"})

print(result)

# final_chain.get_graph().print_ascii()