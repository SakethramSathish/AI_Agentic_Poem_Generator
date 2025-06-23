# AI Agentic Poem Generator

## Overview
AI Agentic Poem Generator is a Streamlit-based web application that generates poems on any topic using advanced AI agents, reviews the generated poem, and (if approved) publishes it to Pastebin. The app leverages Google Generative AI via LangChain and provides a seamless, interactive user experience.

## Features
- **Poem Generation:** Enter any topic and generate a creative poem using AI.
- **Poem Review:** The generated poem is automatically reviewed by an AI agent for quality and relevance.
- **Pastebin Publishing:** If the poem is approved, it is uploaded to Pastebin and a shareable link is provided.
- **User-Friendly UI:** Built with Streamlit for an intuitive and modern web interface.

## Getting Started

### Prerequisites
- Python 3.8+
- Google Generative AI API Key
- Pastebin API Key

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/SakethramSathish/AI_Agentic_Poem_Generator
   cd AI-Agentic-Poem-Generator
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up environment variables:**
   - Create a `.env` file in the project root with the following content:
     ```env
     GOOGLE_API_KEY=your_google_api_key
     PASTEBIN_API_KEY=your_pastebin_api_key
     ```

### Running the App
```bash
streamlit run app.py
```

## Project Structure
```
├── app.py                  # Streamlit app entry point
├── agents/
│   ├── create_poem.py      # Poem generation agent
│   └── review_poem.py      # Poem review agent
├── utils/
│   └── pastebin_uploader.py# Pastebin upload utility
├── requirements.txt        # Python dependencies
└── .env                    # API keys (not committed)
```

## Environment Variables
- `GOOGLE_API_KEY`: Your Google Generative AI API key
- `PASTEBIN_API_KEY`: Your Pastebin API key

## Dependencies
- streamlit
- langchain
- langchain-google-genai
- requests
- python-dotenv

## License
This project is licensed under the MIT License.

## Acknowledgements
- [Streamlit](https://streamlit.io/)
- [LangChain](https://python.langchain.com/)
- [Pastebin](https://pastebin.com/)
- [Google Generative AI](https://ai.google.com/)
