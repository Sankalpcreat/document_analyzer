class MemoryAgent:
    def __init__(self):
        self.memory = {}

    def store_context(self, key, value):
        self.memory[key] = value

    def retrieve_context(self, key):
        return self.memory.get(key, {})
    
