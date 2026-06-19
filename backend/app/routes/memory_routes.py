from fastapi import APIRouter
from app.models.memory import Memory

router = APIRouter()

memories = []

@router.post("/memories")
def create_memory(memory: Memory):
    memories.append(memory)
    return {
        "message": "Memory created",
        "memory": memory
    }

@router.get("/memories")
def get_memories():
    return memories