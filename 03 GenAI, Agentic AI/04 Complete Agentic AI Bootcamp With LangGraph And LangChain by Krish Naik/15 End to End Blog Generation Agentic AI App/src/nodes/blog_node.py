from src.state.blogstate import BlogState, Blog
from langchain_core.messages import HumanMessage


class BlogNode:
    """A class representing a blog node in a content management system."""
    def __init__(self, llm):
        self.llm = llm
      
    # Title generation node  
    def title_generation(self, state: BlogState):
        """Generates a blog title based on the provided topic."""
        if "topic" in state and state["topic"]:
            
            prompt = """Generate a catchy blog title for the following topic: {topic}"""
            
            system_message = prompt.format(topic=state["topic"])
            
            response = self.llm.invoke(system_message)
            
            return {"blog": {"title": response.content}}
        else:
            raise ValueError("Topic is required to generate a blog title.")
        
    # Content generation node  
    def content_generation(self, state: BlogState):
        """Generates blog content based on the provided title."""
        if "topic" in state and state["topic"]:
            prompt = """Generate a detailed blog content for the following topic: {topic}"""
            
            system_message = prompt.format(topic=state["topic"])
            
            response = self.llm.invoke(system_message)
            
            return {"blog": {"title": state["blog"]["title"], "content": response.content}}
        else:
            raise ValueError("Topic is required to generate blog content.")
     
        
    # Translation node 
    def translation(self, state: BlogState):
        """Translates the blog content into a specified language."""
        translation_prompt = """
        Translate the content to the specified language.
        """
        translation_prompt="""
        Translate the following content into {current_language}.
        - Maintain the original tone, style, and formatting.
        - Adapt cultural references and idioms to be appropriate for {current_language}.

        ORIGINAL CONTENT:
        {blog_content}

        """
        
        blog_content = state["blog"]["content"]
        
        messages = [
            HumanMessage(translation_prompt.format(current_language= state["current_language"], blog_content=blog_content))
        ]
        
        transaltion_content = self.llm.with_structured_output(Blog).invoke(messages)
            
        
        
    # Route decision based on current language
    def route(self, state: BlogState):
        """Routes to the appropriate translation node based on the current language."""
        return {"current_language": state["current_language"]}
    
    
    # Route decision function
    def route_decision(self, state: BlogState):
        """Determines the next node based on the current language."""
        if state["current_language"] == "hindi":
            return "hindi"
        elif state["current_language"] == "french":
            return "french"
        else:
            raise ValueError("Unsupported language. Choose 'Hindi' or 'French'.")