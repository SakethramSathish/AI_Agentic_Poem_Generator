from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import StateGraph, END
from utils.pastebin_uploader import upload_to_pastebin
from typing import TypedDict, Optional, List

class PoemState(TypedDict, total=False):
    topic: str
    current_poem: Optional[str]
    last_review: Optional[str]
    history: List[dict]
    paste_url: Optional[str]
    error: Optional[str]

def extract_content(response):
    if isinstance(response, dict) and "content" in response:
        return response["content"].strip()
    try:
        return getattr(response, "content", str(response)).strip()
    except Exception:
        return str(response).strip()
    
llm = ChatGoogleGenerativeAI(model = "gemini-2.0-flash", temperature=0.7)

def generate_poem(state: PoemState) -> PoemState:
    topic = state["topic"]
    history = state.get("history", [])
    last_review = history[-1]["review"] if history else None

    prompt = (
        topic if not last_review else
        f"{topic}\n\nThe previous poem was rejected.\n"
        f"Here is the review:\n{last_review}\n"
        "Please write a new poem that addresses the feedback."
    )

    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "You are a poetic AI. Only output the poem."),
        ("human", "{prompt}")
    ])
    chain = prompt_template | llm

    poem = extract_content(chain.invoke({"prompt": prompt}))
    state["current_poem"] = poem
    return state
def review_poem(state: PoemState) -> PoemState:
    poem = state["current_poem"]
    topic = state["topic"]

    prompt_template = ChatPromptTemplate.from_messages([
        ("system", """You are a critical poetry reviewer. 
        Review the poem and assess structure, creativity, and emotional impact.
        Clearly state if the poem is 'APPROVED' or 'REJECTED' and give reasons."""),
        ("human", "Poem:\n{poem}\n\nTopic: {topic}")
    ])
    chain = prompt_template | llm
    review = extract_content(chain.invoke({"poem": poem, "topic": topic}))
    state["last_review"] = review
    state.setdefault("history", []).append({
        "poem": poem,
        "review": review
    })
    return state

def check_approval(state: PoemState) -> str:
    review = state.get("last_review", "").lower()
    return "approved" if "approved" in review or "publish" in review else "retry"

def publish_poem(state: PoemState) -> PoemState:
    try:
        paste_url = upload_to_pastebin(state["current_poem"],
        title=f"Poem on {state['topic']}")
        state["paste_url"] = paste_url
    except Exception as e:
        state["error"] = str(e)
    return state

def build_graph():
    builder = StateGraph(state_schema=PoemState)

    builder.add_node("generate", generate_poem)
    builder.add_node("review", review_poem)
    builder.add_node("publish", publish_poem)

    builder.set_entry_point("generate")
    builder.add_edge("generate", "review")
    builder.add_conditional_edges("review", check_approval, {
        "approved": "publish", 
        "retry": "generate"
    })
    builder.add_edge("publish", END)

    return builder.compile()