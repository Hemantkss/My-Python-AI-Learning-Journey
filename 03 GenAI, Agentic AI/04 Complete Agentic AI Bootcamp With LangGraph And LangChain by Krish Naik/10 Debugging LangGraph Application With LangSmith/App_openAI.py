from typing import TypedDict, Annotated
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import BaseMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
import requests
import os
from dotenv import load_dotenv
load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')

# Class State
class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

# LLM Model
model = ChatOpenAI()

def build_the_agent():
    """Make a tool-calling agent"""
    
    # Define the tools
    # Add tool
    @tool
    def add(a: float, b: float) -> float:
        """Adds two numbers."""
        return a + b
        

    # Bind tools
    tool_node = ToolNode([add])
    model_with_tools = model.bind_tools([add])
    
    # Agent node
    def call_model(state):
        return {"messages": [model_with_tools.invoke(state["messages"])]}

    # Decide next step
    def should_continue(state: State):
        if state["messages"][-1].tool_calls:
            return "tools"   # go to tool node
        return END            # otherwise finish

    # Build graph
    graph = StateGraph(State)
    
    # Add nodes
    graph.add_node("agent", call_model)
    graph.add_node("tools", tool_node)

    # Add edges
    graph.add_edge(START, "agent")
    graph.add_edge("tools", "agent")
    graph.add_conditional_edges("agent", should_continue, {"tools": "tools", END: END})

    # Compile
    workflow = graph.compile()
    
    return workflow

workflow = build_the_agent()
