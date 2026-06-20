from fastapi import APIRouter
from app.services.memory_service import load_memories

router = APIRouter()

@router.get("/search")
def search_memories(q: str):

    memories = load_memories()

    results = []

    query = q.lower()

    for memory in memories:

        memory_text = str(memory).lower()

        if query in memory_text:
            results.append(memory)

    return results