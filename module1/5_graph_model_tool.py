# here i dint execute the tool, the llm will be able to call the tool but the tool will not be executed in this graph

from langgraph.graph import StateGraph, START, END, MessagesState
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.tools import tool

load_dotenv()

model_llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro")

@tool
def multiply(nb1: int, nb2: int) -> int:
    """This tool is used for multiplying 2 numbers and returning the product"""
    return nb1*nb2

model_llm_with_tool = model_llm.bind_tools([multiply])

# nodes
def chat_with_tool(state: MessagesState) -> MessagesState:
    return {"messages": [model_llm_with_tool.invoke(state["messages"])]}

builder = StateGraph(MessagesState)

builder.add_node("chat_with_tool", chat_with_tool)

builder.add_edge(START, "chat_with_tool")
builder.add_edge("chat_with_tool",END)

graph = builder.compile()