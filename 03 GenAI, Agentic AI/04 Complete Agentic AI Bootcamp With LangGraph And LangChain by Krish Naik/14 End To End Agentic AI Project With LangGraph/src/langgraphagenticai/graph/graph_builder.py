from langgraph.graph import StateGraph, START, END
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphagenticai.tools.search_tool import get_tools, create_tool_node
from langgraph.prebuilt import tools_condition
from src.langgraphagenticai.nodes.chatbot_with_tool_node import ChatbotWithToolNode
from src.langgraphagenticai.nodes.ai_news_node import AINewsNode


class GraphBuilder:
    def __init__(self, model):
        """
        Initialize the GraphBuilder with an LLM model.

        Args:
            model: An LLM instance (e.g., ChatOpenAI).
        """
        if not hasattr(model, "invoke"):
            raise TypeError(
                f"Expected an LLM object with `.invoke()`, got {type(model)}"
            )

        self.llm = model
        self.graph_builder = None

    # ==============================
    # Basic Chatbot Graph
    # ==============================
    def basic_chatbot_build_graph(self):
        # Build the graph
        self.graph_builder = StateGraph(State)
        
        # Basic Chatbot Node
        self.basic_chatbot_node = BasicChatbotNode(self.llm)
        
        # Node
        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)
        
        # Edges
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)

    # ==============================
    # Chatbot With Tools Graph
    # ==============================
    def chatbot_with_tools_build_graph(self):
        # Build the graph
        self.graph_builder = StateGraph(State)
        
        # Chatbot With Tools Node
        tools = get_tools()
        tool_node = create_tool_node(tools)

        obj_chatbot_with_tool_node = ChatbotWithToolNode(self.llm)
        chatbot_node = obj_chatbot_with_tool_node.create_chatbot(tools)
        
        # Nodes
        self.graph_builder.add_node("chatbot", chatbot_node)
        self.graph_builder.add_node("tools", tool_node)
        
        # Edges
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("tools", "chatbot")

    # ==============================
    # AI News Graph
    # ==============================
    def ai_news_build_graph(self):
        # Build the graph
        self.graph_builder = StateGraph(State)
        ai_news_node = AINewsNode(self.llm)

        # Nodes
        self.graph_builder.add_node("fetch_news", ai_news_node.fetch_news)
        self.graph_builder.add_node("summarize_news", ai_news_node.summarize_news)
        self.graph_builder.add_node("save_result", ai_news_node.save_result)

        # Edges
        self.graph_builder.add_edge(START, "fetch_news")
        self.graph_builder.add_edge("fetch_news", "summarize_news")
        self.graph_builder.add_edge("summarize_news", "save_result")
        self.graph_builder.add_edge("save_result", END)

    # ==============================
    # Setup Graph by Use Case
    # ==============================
    def setup_graph(self, usecase: str):
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        elif usecase == "Chatbot With Web":
            self.chatbot_with_tools_build_graph()
        elif usecase == "AI News":
            self.ai_news_build_graph()
        else:
            raise ValueError(f"Unknown usecase: {usecase}")

        return self.graph_builder.compile()
