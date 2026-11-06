# importing our lib
from langchain.graph import StateGraph, START, END

#nodes
def greeting(state:str) ->str:
    """A simple greeting function that returns a greeting to the user."""
    return state + "Hello! How can I assist you today?"


builder = StateGraph(str)

# add nodes to the graph
builder.add_node("greeting", greeting)

# add edges to the graph
builder.add_edge(START, "greeting")
builder.add_edge("greeting", END)

graph = builder.compile()

print(graph.invoke("hey am new"))