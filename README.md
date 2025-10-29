# 🧠 AI Personalities Showcase

A fun Streamlit app that showcases different AI personalities powered by Groq's Llama 3.3 model. Ask questions and get responses from characters like the Cheshire Cat, a Sassy Fairy, a British Pub Chimp, and more!

## ✨ Features

- 🎭 **5 Pre-built Personalities**: Cheshire Cat, Sassy Fairy, British Pub Chimp, Environmental Lawyer, and Custom
- 🤖 **AI-Powered Responses**: Uses Groq's ultra-fast Llama 3.3 (70B) model
- 🎨 **Beautiful UI**: Pre-chosen background or custom gradient background with clean, modern design
- 🆓 **Free to Use**: Groq API offers free tier with generous limits
- 🎮 **Demo Mode**: Works without API key using pre-written example responses
- 🛠️ **Custom Personalities**: Create your own unique AI character

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-personalities-showcase.git
cd ai-personalities-showcase
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Get Your Free Groq API Key

1. Go to [Groq Console](https://console.groq.com)
2. Sign up for a free account
3. Navigate to API Keys section
4. Create a new API key (starts with `gsk_`)

### 4. Configure Secrets

Create a `.streamlit` folder and add your API key:

```bash
mkdir .streamlit
```

Create `.streamlit/secrets.toml` with:

```toml
GROQ_API_KEY = "gsk_your_api_key_here"
```

### 5. Run the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 🎭 Available Personalities

| Personality | Description |
|------------|-------------|
| 😼 **Cheshire Cat** | Mysterious and philosophical, speaks in riddles |
| 🧚 **Sassy Fairy** | Sarcastic and eye-rolling, tired of mortals |
| 🐵 **British Pub Chimp** | Drunk pub philosopher, confidently incorrect |
| ⚖️ **Environmental Lawyer** | Condescending legal expert, $500/hour energy |
| 🎭 **Custom** | Create your own unique personality |

## 🎮 Demo Mode

Don't have an API key yet? No problem! The app works in **Demo Mode** with pre-written responses so you can test the interface before setting up your API key.

## 🎨 Customization

### Add a Custom Background

Place a `background.png` image in the root directory. If no image is found, the app uses a beautiful purple gradient by default.

### Create Custom Personalities

Select "Custom" from the dropdown and define:
- **Role**: Who the AI should be (e.g., "You are a pirate captain")
- **Style**: How they should respond (e.g., "Use pirate slang and talk about treasure")

## 📁 Project Structure

```
ai-personalities-showcase/
├── app.py                    # Main application file
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore rules
├── README.md                # This file
├── .streamlit/
│   └── secrets.toml         # API keys (not tracked in git)
└── background.png           # Optional custom background
```

## 🔧 Configuration

### API Settings

The app uses these Groq API parameters:
- **Model**: `llama-3.3-70b-versatile`
- **Temperature**: 0.9 (creative responses)
- **Max Tokens**: 200 (2-3 sentence responses)
- **Top P**: 0.9

You can modify these in the `ask_ai_groq()` function in `app.py`.

## 🐛 Troubleshooting

### "Invalid API key" error
- Check that your API key starts with `gsk_`
- Verify the key is correctly added to `.streamlit/secrets.toml`
- Try regenerating your API key in Groq Console

### "Rate limit reached" error
- Groq's free tier has rate limits
- Wait a moment and try again
- Consider upgrading to a paid tier if needed

### Import errors
- Make sure you've installed all dependencies: `pip install -r requirements.txt`
- Try creating a virtual environment

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add new personalities
- Improve the UI/UX
- Fix bugs
- Enhance documentation

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

**Chris G.**

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [Groq](https://groq.com/) & Llama 3.3
- Inspired by the fun of AI personalities

## 📞 Support

If you encounter issues:
1. Check the [Troubleshooting](#-troubleshooting) section
2. Review [Groq's documentation](https://console.groq.com/docs)
3. Open an issue on GitHub

---

⭐ If you find this project helpful, please give it a star!