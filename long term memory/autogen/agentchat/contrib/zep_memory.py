import os
import logging
from zep_cloud.client import AsyncZep
from zep_cloud.memory import MemorySearchPayload
from autogen.memory import BaseMemory

logger = logging.getLogger(__name__)


class ZepMemory(BaseMemory):
    def __init__(
        self,
        session_id: str,
        memory_type: str = "permanent",
        memory_retrieval: str = "default",
        relevance_threshold: float = 0.3,
        summary_instruction: str = "",
    ):
        self.session_id = session_id
        self.zep = AsyncZep(api_key=os.getenv("ZEP_API_KEY"))
        self.memory_type = memory_type
        self.memory_retrieval = memory_retrieval
        self.relevance_threshold = relevance_threshold
        self.summary_instruction = summary_instruction
        logger.info(f"ZepMemory initialized for session: {session_id}")

    def save_message(self, role: str, message: str) -> None:
        """Saves a message to Zep memory."""
        logger.debug(f"Saving message to Zep: role={role}, message={message}")
        self.zep.memory.add_memory(
            session_id=self.session_id,
            role=role,
            content=message,
        )

    def retrieve_memories(self, query: str) -> str:
        """Retrieves relevant memory from Zep."""
        logger.debug(f"Retrieving memory for query: {query}")
        payload = MemorySearchPayload(
            session_id=self.session_id,
            messages=[],
            top_k=5,
            threshold=self.relevance_threshold,
        )
        results = self.zep.memory.search_memory(payload)
        facts = [m.content for m in results.messages]
        return "\n".join(facts)

    def to_dict(self):
        return {
            "session_id": self.session_id,
            "memory_type": self.memory_type,
            "memory_retrieval": self.memory_retrieval,
        }
