from src.langgraphagenticai.state.state import State

class ChatbotWithToolNode:
    """
    A node that integrates a chatbot with tool capabilities.
    """

    def __init__(self, model):
        self.llm = model   # MUST be a ChatOpenAI (not a dict!)
        print("DEBUG -> LLM type:", type(model))

    def process(self, state: State):
        """
        Process the input state and generate a response.
        """
        user_input = state["messages"][-1]["content"] if state["messages"] else ""
        llm_response = self.llm.invoke([{"role": "user", "content": user_input}])

        # simulate tool-specific logic
        tool_response = f"Tool response for input: {user_input}"

        return {"messages": [llm_response, tool_response]}

    def create_chatbot(self, tools):
        """
        Create a chatbot node with tool capabilities.
        """
        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state: State):
            return {"messages": [llm_with_tools.invoke(state["messages"])]}

        return chatbot_node
