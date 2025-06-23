import streamlit as st
from agents.create_poem import get_poem_agent
from agents.review_poem import get_review_agent
from utils.pastebin_uploader import upload_to_pastebin
from dotenv import load_dotenv
import os

load_dotenv()
st.set_page_config(page_title="AI Poetry Generator", layout="centered")
st.title("📝 AI Poem Generator and Reviewer")

# Utility function to extract clean content
def extract_content(response):
    if isinstance(response, dict) and "content" in response:
        return response["content"].strip()
    try:
        return getattr(response, "content", str(response)).strip()
    except Exception:
        return str(response).strip()

topic = st.text_input("Enter a topic for the poem")

if st.button("Generate Poem"):
    if not topic.strip():
        st.warning("Please enter a topic first.")
    else:
        # Step 1: Generate Poem
        with st.spinner("Generating poem..."):
            poem_agent = get_poem_agent()
            raw_poem_response = poem_agent.invoke({"topic": topic})
            poem = extract_content(raw_poem_response)

        st.subheader("📜 Generated Poem")
        st.markdown(f"**_Poem on {topic}_**\n\n{poem}", unsafe_allow_html=True)

        # Step 2: Review Poem
        with st.spinner("Reviewing poem..."):
            review_agent = get_review_agent()
            raw_review_response = review_agent.invoke({
                "poem": poem,
                "topic": topic,
                "intermediate_steps": []
            })
            review = extract_content(raw_review_response)

        st.subheader("🧐 Poem Review")
        st.markdown(review, unsafe_allow_html=True)

        # Step 3: Conditional Upload
        if "approved" in review.lower() or "publish" in review.lower():
            with st.spinner("Uploading to Pastebin..."):
                try:
                    paste_url = upload_to_pastebin(poem, title=f"Poem on {topic}")
                    st.success("Poem approved and published!")
                    st.markdown(f"🔗 [View Published Poem]({paste_url})")
                except Exception as e:
                    st.error(f"Failed to upload to Pastebin: {e}")
        else:
            st.info("Poem not approved for publishing.")
            
