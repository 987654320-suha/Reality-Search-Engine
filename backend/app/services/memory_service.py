import json
from pathlib import Path

DATA_FILE = Path("data/memories.json")

def load_memories():
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_memory(memory):
    memories = load_memories()
    memories.append(memory)

    with open(DATA_FILE, "w") as file:
        json.dump(memories, file, indent=4)