import time
from fastapi import APIRouter

from app.services.memory_service import load_memories
from ai.semantic_search import semantic_search

router = APIRouter()


@router.get("/search")
def search_memories(q: str):

    start = time.time()

    memories = load_memories()

    query_lower = q.lower()

    # Fast keyword search first
    keyword_results = []

    for memory in memories:

        text = (
            memory.get("title", "") + " " +
            memory.get("description", "")
        ).lower()

        if query_lower in text:
            keyword_results.append(memory.copy())

    # If keyword results found, skip AI search
    if keyword_results:
        results = keyword_results[:5]
    else:
        results = semantic_search(
            q,
            memories
        )

    # Cleanup response
    for memory in results:

        memory.pop("embedding", None)

        if len(memory.get("description", "")) > 150:
            memory["description"] = (
                memory["description"][:150] + "..."
            )

    print(
        "SEARCH TOOK:",
        round(time.time() - start, 2),
        "seconds"
    )

    return results