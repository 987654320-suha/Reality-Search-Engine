from ai.embedding_service import get_embedding

embedding = get_embedding(
    "Researching universities in Germany"
)

print(len(embedding))
print(embedding[:10])