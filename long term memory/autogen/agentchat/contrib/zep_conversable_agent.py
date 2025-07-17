from autogen import ConversableAgent
from zep_python import ZepClient
from zep_python.memory import MemorySearchPayload

class ZepConversableAgent(ConversableAgent):
    def __init__(self, name, zep_client: ZepClient, **kwargs):
        super().__init__(name=name, **kwargs)
        self.zep_client = zep_client
        self.memory_retrieval = True

    def retrieve_history(self, messages=None):
        if messages is not None:
            return messages

        try:
            search_results = self.zep_client.memory.search_memory(
                session_id=self.name,
                payload=MemorySearchPayload(
                    text="",
                    metadata={},
                    top_k=5,
                ),
            )
            results = [
                {"role": "assistant", "content": m.message.content}
                for m in search_results
            ]
            return results
        except Exception as e:
            print(f"Zep memory search failed: {e}")
            return []

    def store_message(self, message):
        try:
            self.zep_client.memory.add_memory(
                session_id=self.name,
                messages=[message],
            )
        except Exception as e:
            print(f"Zep memory storage failed: {e}")
