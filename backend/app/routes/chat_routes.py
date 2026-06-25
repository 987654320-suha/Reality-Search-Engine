from fastapi import APIRouter
from pydantic import BaseModel

from app.services.memory_service import load_memories
from app.services.chat_history import (
    add_message,
    get_history,
)

from ai.semantic_search import semantic_search
from ai.chat_service import ask_llama

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
def chat(request: ChatRequest):

    # Load all memories
    memories = load_memories()

    # Save user's message
    add_message(
        "user",
        request.question
    )

    # Retrieve relevant memories
    results = semantic_search(
        request.question,
        memories
    )

    # Get previous conversation
    history = get_history()

    conversation = ""

    for message in history:

        conversation += (
            f"{message['role'].upper()}: "
            f"{message['content']}\n"
        )

    # DEBUG
    print("\n========== SEARCH RESULTS ==========\n")

    for memory in results:
        print(memory.get("title"))

    print("\n===================================\n")

    # Build memory context
    context = ""

    for i, memory in enumerate(results[:5], start=1):

        context += f"""
Memory {i}

Title:
{memory.get("title")}

Description:
{memory.get("description")}

Objects:
{memory.get("objects")}
"""

    # Build final prompt
    prompt = f"""
You are an intelligent personal memory assistant.

Below is the previous conversation.

------------------------
{conversation}
------------------------

Below are the retrieved memories.

------------------------
{context}
------------------------

Answer using BOTH the conversation and the retrieved memories.

If the answer is not present, reply exactly:

"I couldn't find that information."

Question:

{request.question}
"""

    # Ask Llama
    answer = ask_llama(prompt)

    # Save assistant response
    add_message(
        "assistant",
        answer
    )
    return {
    "answer": answer,

    "sources": [
        {
            "title": memory.get("title"),
            "source": memory.get("source")
        }

        for memory in results
    ]
}