import streamlit as st
from dotenv import load_dotenv
from langgraph_runner import get_approval_agent

load_dotenv()
st.set_page_config(page_title = "AI Poetry Generator", layout = "centered")
st.title("AI Poem Generator and Reviewer")

topic = st.text_input("Enter a topic for the poem:")

if st.button("Generate Poem"):
    if not topic.strip():
        st.warning("Please enter a topic first.")
    else:
        with st.spinner("Generating poem and reviewing..."):
            orchestrator = get_approval_agent()
            result = orchestrator({"topic": topic})

        for i, version in enumerate(result.get("history", []), 1):
            st.markdown(f"---\n### Poem Version {i}")
            st.markdown(f"<div style='white-space: pre-wrap;'>{version['poem']}</div>", unsafe_allow_html=True)
            st.markdown(f"### Review {i}")
            st.markdown(f"<div style='white-space: pre-wrap;'>{version['review']}</div>", unsafe_allow_html=True)

        if result.get("paste_url"):
            st.success("Poem approved and published!")
            st.markdown(f"🔗 [View Published Poem]({result['paste_url']})")
        elif result.get("error"):
            st.error(f"❌ {result['error']}")
        else:
            st.warning("Poem was not approved after all attempts.")