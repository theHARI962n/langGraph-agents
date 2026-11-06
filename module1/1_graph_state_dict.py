from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict


#state
class State(TypedDict):
    graph_state: str

# node
def greeting(state: State) -> State:
    """A simple greeting function that returns a greeting to the user."""
    return {"graph_state": state["graph_state"] + "Hello! How can I assist you today?"}


# edges


# putting our graph together
builder = StateGraph(State)

# add nodes to the graph
builder.add_node("greeting", greeting)

# add edges to the graph
builder.add_edge(START, "greeting")
builder.add_edge("greeting", END)

graph = builder.compile()

