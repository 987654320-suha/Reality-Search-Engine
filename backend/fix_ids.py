import json
import uuid

FILE = "data/memories.json"

with open(FILE, "r", encoding="utf-8") as f:
    memories = json.load(f)

for memory in memories:

    if "id" not in memory:

        memory["id"] = str(
            uuid.uuid4()
        )

with open(FILE, "w", encoding="utf-8") as f:

    json.dump(
        memories,
        f,
        ensure_ascii=False,
        indent=4
    )

print(
    "IDs added successfully"
)