from src.agents.chat_agents.graph import create_chat_agent_graph

graph = create_chat_agent_graph()

def chat_agent_handler(message: str) -> dict[str,str]:
    """
    """
    
    return graph.invoke({"message":message})
    
    