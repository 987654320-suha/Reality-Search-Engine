from fastapi import APIRouter
from app.models.memory import Memory
from app.services.memory_service import (
    load_memories,
    save_memory,
)

router = APIRouter()


@router.post("/memories")
def create_memory(memory: Memory):

    save_memory(memory.model_dump())

    return {
        "message": "Memory created",
        "memory": memory
    }


@router.get("/memories")
def get_memories():

    return load_memories()