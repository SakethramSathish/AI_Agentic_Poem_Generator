from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable
from dotenv import load_dotenv 

load_dotenv()

def get_review_agent() -> Runnable:
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.7)

    review_prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a discerning and critical poetry reviewer. Review the following poem for:
        - Structure
        - Language
        - Theme and Creativity

        Give an honest and helpful review. If it's excellent and publish-worthy, say so clearly. Otherwise, suggest improvements.
        """),
        ("human", "Poem:\n{poem}\n\nTopic: {topic}")
    ])

    return review_prompt | llm
