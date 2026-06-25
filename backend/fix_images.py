import json

with open("data/memories.json", "r", encoding="utf-8") as f:
    memories = json.load(f)

for memory in memories:

    if memory.get("source"):
        memory["image"] = f"/uploads/{memory['source']}"

with open("data/memories.json", "w", encoding="utf-8") as f:
    json.dump(
        memories,
        f,
        indent=4,
        ensure_ascii=False
    )

print("Image paths added!")