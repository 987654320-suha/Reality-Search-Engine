chat_history = []


def add_message(role, content):

    chat_history.append({
        "role": role,
        "content": content
    })

    # Keep only last 10 messages
    if len(chat_history) > 10:
        chat_history.pop(0)


def get_history():

    return chat_history


def clear_history():

    chat_history.clear()