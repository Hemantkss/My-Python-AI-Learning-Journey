from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    Returns a list of tools to be used in the graph.
    Currently, it includes the Tavily Search tool for web search capabilities.
    """
    
    tools = [TavilySearchResults(max_results= 2)]
    
    return tools

def create_tool_node(tools):
    """
    Creates a ToolNode using the provided tools.
    
    Args:
        tools (list): A list of tool instances to be included in the ToolNode.
        
    Returns:
        ToolNode: An instance of ToolNode initialized with the given tools.
    """
    
    return ToolNode(tools=tools)