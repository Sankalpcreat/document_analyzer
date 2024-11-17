class MemoryAgent:
    def __init__(self):
        self.memory = {}

    def store_context(self, key, value):
       
        if not key:
            raise ValueError("Key cannot be empty.")
        self.memory[key] = value

    def retrieve_context(self, key):
        
        if not key:
            raise ValueError("Key cannot be empty.")
        return self.memory.get(key, {})

    def clear_memory(self):
        
        self.memory.clear()