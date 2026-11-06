from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict
from typing import Literal

#state
class State(TypedDict):
    graph_state: str

# nodes
def node1(state: State) -> State:
    """A simple greeting function that returns a greeting to the user."""
    return {"graph_state": state["graph_state"] + "Hello! How can I assist you today?"}

def node2(state: State) -> State:
    """this is a node greet our user """
    return {"graph_state": state["graph_state"] + "I am in node2"}

def node3(state: State) -> State:
    """this is a node greet our user """
    return {"graph_state": state["graph_state"] + "I am in node3"}

#edges
def next_step(state: State) -> Literal["node2", "node3"]:
    """this is a edge function to decide which node to go next"""
    state_str = state["graph_state"]
    array_state_str = state_str.split(" ")

    if array_state_str[0] == "Hello!":
        return "node2"
    else:
        return "node3"

# putting our graph together
builder = StateGraph(State)

# add nodes to the graph
builder.add_node("node1", node1)
builder.add_node("node2", node2)
builder.add_node("node3", node3)

# add edges to the graph
builder.add_edge(START, "node1")
builder.add_conditional_edges("node1", next_step, {"node2": "node2", "node3": "node3"})
builder.add_edge("node2", END)
builder.add_edge("node3", END)

graph = builder.compile()

 