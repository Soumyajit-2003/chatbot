from src.agents.chat_agents.graph import create_chat_agent_graph
from langchain.messages import HumanMessage
from src.agents.chat_agents.states.chat_agent_state import ChatAgentState

graph = create_chat_agent_graph()

def chat_agent_handler(thread_id: str,message:str) -> ChatAgentState:
    """
    """
    
    return graph.invoke(
        input={
            "message":[HumanMessage(content=message)],
        },
        config={
            "configurable": {"thread_id": thread_id},
        },
    )
    
def get_all_threads_handler() -> list[str | None]:
    """
    
    """
    all_checkpoints = graph.checkpointer.list(config={})

    threads = set()


    for checkpoint in all_checkpoints:
        threads.add(checkpoint.config["configurable"]["thread_id"])

    return list(threads)

def chat_history_handler(thread_id: str) ->ChatAgentState:
    """
    """
    # Placeholder implementation
    return graph.get_state(config={"configurable": {"thread_id": thread_id}})[0]
    