memory_store = {}


def save_memory(user, data):

    memory_store[user] = data

    return {
        "message": "Memory saved successfully"
    }


def get_memory(user):

    return memory_store.get(user, {})