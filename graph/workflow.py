from langgraph.graph import StateGraph, END

from utils.state import AgentState

from agents.csv_loader_agent import csv_loader_agent
from agents.analytics_agent import analytics_agent
from agents.response_agent import response_agent


workflow = StateGraph(AgentState)

# Nodes
workflow.add_node(
    "load_csv",
    csv_loader_agent
)

workflow.add_node(
    "analyze",
    analytics_agent
)

workflow.add_node(
    "respond",
    response_agent
)

# Entry Point
workflow.set_entry_point("load_csv")

# Edges
workflow.add_edge(
    "load_csv",
    "analyze"
)

workflow.add_edge(
    "analyze",
    "respond"
)

workflow.add_edge(
    "respond",
    END
)

graph = workflow.compile()