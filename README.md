# LinkedIn Human Post Writer

[![Live Demo](https://img.shields.io/badge/Live%20Demo-humangpt.streamlit.app-brightgreen?style=for-the-badge)](https://humangpt.streamlit.app)

A CLI and Web UI tool that generates LinkedIn posts using OpenAI GPT-4o and ensures they sound human by checking with OpenAI's own detection capabilities.

## Features
- Generates LinkedIn posts from your prompt
- Checks if the post sounds AI-written using OpenAI
- Humanizes the post if needed
- Use via CLI or a modern web UI (Streamlit)

## Setup
1. Clone the repo
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_openai_key
   ```

## Usage

### Run the CLI
```bash
python main.py
```
Follow the prompts to generate your LinkedIn post.

### Run the Web UI (Streamlit)
```bash
streamlit run app.py
```
- This command starts a local server and prints a URL (usually http://localhost:8501) in your terminal.
- **Open your browser and go to that URL** to use the app.
- The terminal must remain open while you use the app in your browser.

## Troubleshooting
- If you see a "Safari Can't Connect to the Server" or similar error, make sure:
  - The terminal running `streamlit run app.py` is still open and shows no errors.
  - You are using the correct URL and port (check the terminal output for the exact address).
  - There are no errors in the terminal. If there are, copy them and seek help.
- If you have issues with API keys, double-check your `.env` file and ensure your OpenAI key is valid.

## Notes
- The AI detection is performed by prompting OpenAI to analyze the text and judge if it is AI- or human-written.
- No external AI detection API (like ZeroGPT) is used; only your OpenAI API key is required.

---

Feel free to open issues or contribute improvements!