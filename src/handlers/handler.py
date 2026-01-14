from src.agents.chat_agents.graph import create_chat_agent_graph
from langchain.messages import HumanMessage
from src.agents.chat_agents.states.chat_agent_state import ChatAgentState

graph = create_chat_agent_graph()

def chat_agent_handler(message: str) -> ChatAgentState:
    """
    """
    
    return graph.invoke({"message":[HumanMessage(content=message)]})
    
    