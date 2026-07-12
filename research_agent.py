from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

class ResearchAgent:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flashexit"
        )

    def research(self, query):
        messages = [
            SystemMessage(
                content="You are an AI Research Agent. Provide accurate, concise and factual answers."
            ),
            HumanMessage(content=query)
        ]

        response = self.llm.invoke(messages)
        return response.content