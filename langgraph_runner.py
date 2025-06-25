from agents.langgraph_poem_graph import build_graph

def get_approval_agent():
    graph = build_graph()
    return lambda inputs: graph.invoke(inputs)