from fastapi import APIRouter
from app.services.memory_service import load_memories

router = APIRouter()

@router.get("/timeline")
def timeline():

    memories = load_memories()

    memories.sort(
        key=lambda x: x.get("date", "9999-99-99")
    )

    return memories