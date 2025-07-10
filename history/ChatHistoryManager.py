import json
import os
from langchain.schema import HumanMessage, AIMessage, SystemMessage

class ChatHistoryManager:
    def __init__(self, filepath="data/chat_history.json"):
        self.filepath = filepath

    def load(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r", encoding="utf-8") as f:
                raw = json.load(f)
                return [
                    HumanMessage(m["content"]) if m["role"] == "user"
                    else AIMessage(m["content"]) if m["role"] == "assistant"
                    else SystemMessage(m["content"])
                    for m in raw
                ]
        else:
            return [SystemMessage(content="You are a helpful assistant for post-surgery recovery.")]

    def save(self, messages):
        serializable = []
        for m in messages:
            role = (
                "user" if isinstance(m, HumanMessage)
                else "assistant" if isinstance(m, AIMessage)
                else "system"
            )
            serializable.append({"role": role, "content": m.content})

        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(serializable, f, ensure_ascii=False, indent=2)
