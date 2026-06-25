from fastapi import APIRouter
from fastapi import HTTPException

from app.services.memory_service import (
    load_memories
)

router = APIRouter()


@router.get("/memory/{memory_id}")
def get_memory(memory_id: str):

    memories = load_memories()

    for memory in memories:

        if memory.get("id") == memory_id:

            memory.pop(
                "embedding",
                None
            )

            return memory

    raise HTTPException(
        status_code=404,
        detail="Memory not found"
    )