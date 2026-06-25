from fastapi import APIRouter

from app.services.memory_service import (
    load_memories
)

router = APIRouter()


@router.get("/stats")
def get_stats():

    memories = load_memories()

    total = len(memories)

    images = 0
    pdfs = 0
    docx = 0

    for memory in memories:

        if memory.get("image"):
            images += 1

        if memory.get("file_type") == "pdf":
            pdfs += 1

        if memory.get("file_type") == "docx":
            docx += 1

    return {
        "total": total,
        "images": images,
        "pdfs": pdfs,
        "docx": docx
    }