# Agentic AI Poem Generator 5.0

A modular, agentic AI-powered poetry generator and reviewer built with LangChain, LangGraph, and Streamlit. This project generates original poems on any topic, reviews them with strict criteria, and publishes approved poems to Pastebin.

## Features
- **AI Poem Generation:** Uses Google Gemini via LangChain to generate creative poems on user-specified topics.
- **Automated Review:** Critically reviews poems for structure, creativity, emotional impact, and adherence to requirements.
- **Agentic Workflow:** Utilizes LangGraph to orchestrate the generation, review, and publishing process.
- **Pastebin Publishing:** Publishes approved poems to Pastebin and returns a shareable link.
- **Streamlit UI:** Simple web interface for user interaction.

## Requirements
- Python 3.8+
- See `requirements.txt` for Python dependencies.

## Installation
1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd Agentic-AI-Poem-Generator-5.0
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Set up environment variables:**
   - Create a `.env` file in the project root.
   - Add your Google Gemini API key and Pastebin API key:
     ```env
     GOOGLE_API_KEY=your_google_api_key
     PASTEBIN_API_KEY=your_pastebin_api_key
     ```

## Usage
1. **Run the Streamlit app:**
   ```sh
   streamlit run app.py
   ```
2. **Enter a topic** and let the agent generate, review, and publish a poem.
3. **Get a Pastebin link** to the approved poem.

## Project Structure
```
app.py                      # Streamlit UI
langgraph_runner.py         # Orchestrator for the agentic workflow
agents/
  langgraph_poem_graph.py   # Core agent logic (generation, review, publish)
utils/
  pastebin_uploader.py      # Pastebin integration
requirements.txt            # Python dependencies
```

## Customization
- **Review Criteria:** Edit `agents/langgraph_poem_graph.py` to adjust poem requirements or review strictness.
- **Pastebin Integration:** Update `utils/pastebin_uploader.py` for custom publishing logic.

## License
MIT License

## Acknowledgements
- [LangChain](https://github.com/langchain-ai/langchain)
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [Streamlit](https://streamlit.io/)
- [Google Gemini](https://ai.google.dev/)
- [Pastebin](https://pastebin.com/)
