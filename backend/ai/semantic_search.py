from ai.embedding_service import get_embedding
import numpy as np


def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)

    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )


def semantic_search(query, memories):

    query_embedding = get_embedding(query)

    scored = []

    for memory in memories:

        if "embedding" not in memory:
            continue

        score = cosine_similarity(
            query_embedding,
            memory["embedding"]
        )

        print(
            round(score, 3),
            "->",
            memory["title"]
        )

        scored.append((score, memory))

    scored.sort(
        key=lambda x: x[0],
        reverse=True
    )

    results = []

    for score, memory in scored:

        if score > 0.35:

            memory_copy = memory.copy()

            memory_copy.pop("embedding", None)

            if len(memory_copy.get("description", "")) > 150:
                memory_copy["description"] = (
                    memory_copy["description"][:150] + "..."
                )

            results.append(memory_copy)

        if len(results) >= 5:
            break

    return results