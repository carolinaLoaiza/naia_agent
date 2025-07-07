from langchain.schema import HumanMessage, AIMessage, SystemMessage
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

class GroqChat:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("GROQ_API_KEY")
        self.llm = ChatGroq(groq_api_key=self.api_key, temperature=0.5, model="llama-3.1-8b-instant")

    def get_initial_messages(self):
        return [
            SystemMessage(content="You are a helpful assistant for post-surgery recovery.")
        ]

    def human_message(self, content):
        return HumanMessage(content=content)

    def ai_message(self, content):
        return AIMessage(content=content)

    def get_response(self, messages):
        return self.llm.invoke(messages).content
