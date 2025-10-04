class ChatMemory:
    def __init__(self, max_turns=3):
        self.max_turns = max_turns
        self.history = []

    def add_message(self, role, message):
        self.history.append({"role": role, "message": message})
        if len(self.history) > self.max_turns * 2:  
            self.history.pop(0)

    def get_context(self):
        if not self.history:
            return ""
        return " ".join(f"{turn['role']}: {turn['message']}" for turn in self.history)
