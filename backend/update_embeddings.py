from app.services.memory_service import load_memories
from ai.embedding_service import get_embedding
import json

memories = load_memories()

for memory in memories:

    text = (
        memory.get("title", "") + " " +
        memory.get("description", "")
    )

    memory["embedding"] = get_embedding(text)

with open(
    "data/memories.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        memories,
        f,
        ensure_ascii=False,
        indent=4
    )

print("Embeddings updated!")