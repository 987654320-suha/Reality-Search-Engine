import json
import uuid
from pathlib import Path

from ai.embedding_service import get_embedding

DATA_FILE = Path("data/memories.json")


def load_memories():

    if not DATA_FILE.exists():
        return []

    with open(
        DATA_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def save_memory(memory):

    # Generate unique ID
    if "id" not in memory:

        memory["id"] = str(
            uuid.uuid4()
        )

    text = (
        memory.get("title", "")
        + " "
        + memory.get(
            "description",
            ""
        )
    )

    memory["embedding"] = (
        get_embedding(text)
    )

    memories = load_memories()

    memories.append(memory)

    with open(
        DATA_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            memories,
            f,
            ensure_ascii=False,
            indent=4
        )