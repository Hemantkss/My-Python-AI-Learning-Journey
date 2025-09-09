from langgraph.graph import StateGraph, START, END
from src.llms.openai_llm import OpenAI_LLM
from src.state.blogstate import BlogState
from src.nodes.blog_node import BlogNode

class GraphBuilder:
    def __init__(self, llm):
        self.llm = llm
        self.graph = StateGraph(BlogState)

    # Simple blog generation graph
    def build_topic_graph(self):
        """Builds a  graph for generating blog topics."""
        
        blog_node_obj = BlogNode(self.llm)
        
        # Nodes
        self.graph.add_node("title_generation", blog_node_obj.title_generation)
        self.graph.add_node("content_generation", blog_node_obj.content_generation)
        
        # Edges
        self.graph.add_edge(START, "title_generation")
        self.graph.add_edge("title_generation", "content_generation")
        self.graph.add_edge("content_generation", END)
        
       
        return self.graph
    
    # Blog generation in different language
    def build_language_graph(self):
        """Builds a  graph for generating blog in different language."""
        
        blog_node_obj = BlogNode(self.llm)
        
        # Nodes
        self.graph.add_node("title_generation", blog_node_obj.title_generation)
        self.graph.add_node("content_generation", blog_node_obj.content_generation)
        
        self.graph.add_node("hindi_translation", lambda state: blog_node_obj.translation({**state, "current_language": "hindi"}))
        self.graph.add_node("french_translation", lambda state: blog_node_obj.translation({**state, "current_language": "french"}))
        self.graph.add_node("route", blog_node_obj.route)
        
        # Edges
        self.graph.add_edge(START, "title_generation")
        self.graph.add_edge("title_generation", "content_generation")
        self.graph.add_edge("content_generation", "route")
        
        self.graph.add_conditional_edges(
            "route",
            blog_node_obj.route_decision,
            {
                "hindi": "hindi_translation",
                "french": "french_translation"
            }
        )
        self.graph.add_edge("hindi_translation", END)
        self.graph.add_edge("french_translation", END)
        
        return self.graph
    
    # Graph compilation based on usecase
    def setup_graph(self, usecase):
        if usecase == "topic":
            self.build_topic_graph()
            
        elif usecase == "language":
            self.build_language_graph()
        else:
            raise ValueError("Invalid usecase. Choose 'topic' or 'language'.")
            
        return self.graph.compile()
    
    
# Below code is for langgraph Studio integration
llm = OpenAI_LLM().get_llm()
graph_builder = GraphBuilder(llm)
graph = graph_builder.build_language_graph().compile()
        