from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()
# ------------------------
# 1. Define State
# ------------------------
class State(TypedDict):
    messages: Annotated[list, "Conversation history"]
    poem: str

# ------------------------
# 2. LLM Setup
# ------------------------
llm = ChatOpenAI(model="gpt-4o-mini")  # or "gpt-3.5-turbo"

# ------------------------
# 3. Poem Generator Node
# ------------------------
def poem_node(state: State) -> State:
    user_request = state["messages"][-1].content
    response = llm.invoke([HumanMessage(content=f"Write a short poem about: {user_request}")])
    poem_text = response.content
    state["poem"] = poem_text
    state["messages"].append(AIMessage(content=poem_text))
    return state

# ------------------------
# 4. Human-in-the-loop Node
# ------------------------
def human_check_node(state: State) -> State:
    while True:
        print("\n--- Human Checkpoint ---")
        print(f"\nAI Poem:\n{state['poem']}")
        choice = input("\nApprove (y) / Reject (n) / Edit (e): ")

        if choice.lower() == "y":
            print("✅ Poem Approved!")
            break
        elif choice.lower() == "n":
            print("🔄 Regenerating poem...")
            # Ask LLM to regenerate poem
            last_msg = state["messages"][0].content
            response = llm.invoke([HumanMessage(content=f"Regenerate a different poem about: {last_msg}")])
            state["poem"] = response.content
            state["messages"].append(AIMessage(content=response.content))
        elif choice.lower() == "e":
            new_poem = input("✍️ Enter your edited poem: ")
            state["poem"] = new_poem
            print("✅ Poem Edited by Human!")
            break
        else:
            print("⚠️ Invalid choice, try again.")
    return state

# ------------------------
# 5. Build LangGraph
# ------------------------
graph = StateGraph(State)
graph.add_node("poem", poem_node)
graph.add_node("human_check", human_check_node)

graph.add_edge(START, "poem")
graph.add_edge("poem", "human_check")
graph.add_edge("human_check", END)

app = graph.compile()

# ------------------------
# 6. Run Example
# ------------------------

topic = str(input("Enter a topic: "))
state = {"messages": [HumanMessage(content=topic)], "poem": ""}
final_state = app.invoke(state)

print("\n--- Final Approved Poem ---")
print(final_state["poem"])

