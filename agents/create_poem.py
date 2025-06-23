from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_tool_calling_agent
from langchain_core.runnables import Runnable
from dotenv import load_dotenv

load_dotenv()

def get_poem_agent() -> Runnable:
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature = 0.7)

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a creative poet. Write a beautiful, original poem when the user provides a topic. And you should provide the poem only and nothing else."),
        ("human", "{topic}")
    ])

    agent = prompt | llm
    return agent