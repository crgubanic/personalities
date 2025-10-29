import base64
import streamlit as st
from pathlib import Path
import requests
import json

# ----------------------------
# Configuration
# ----------------------------
try:
    GROQ_API_KEY = st.secrets.get("GROQ_API_KEY", "")
    USE_AI = bool(GROQ_API_KEY)
except:
    GROQ_API_KEY = ""
    USE_AI = False

# ----------------------------
# AI Response Function - Groq (Free & Fast!)
# ----------------------------
def ask_ai_groq(personality_role: str, personality_style: str, user_input: str) -> str:
    """Generate response using Groq API with Llama model."""
    
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Craft the system prompt
    system_prompt = f"{personality_role}. {personality_style} Keep your response to 2-3 sentences maximum. Stay fully in character and be entertaining."
    
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.9,
        "max_tokens": 200,
        "top_p": 0.9
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            return result["choices"][0]["message"]["content"].strip()
        elif response.status_code == 401:
            return "⚠️ Invalid API key. Please check your Groq API key in secrets.toml"
        elif response.status_code == 429:
            return "⏱️ Rate limit reached. Please wait a moment and try again."
        else:
            error_msg = response.json().get("error", {}).get("message", "Unknown error")
            return f"⚠️ API Error ({response.status_code}): {error_msg}"
            
    except requests.exceptions.Timeout:
        return "⏱️ Request timed out. Please try again."
    except Exception as e:
        return f"❌ Error: {str(e)}"

# ----------------------------
# Demo Mode Responses (when no API key)
# ----------------------------
def get_demo_response(personality_key: str) -> str:
    """Return demo response when API is not configured."""
    demos = {
        "cheshire_cat": "Ah, curious questions lead to curious places, don't they? The answer appears only to those who've already forgotten what they were looking for. Rather convenient, wouldn't you say? 😼",
        "sassy_fairy": "Oh wonderful, another question. *rolls eyes* Have you tried using that thing between your ears called common sense? But fine, I'll help—this time. You're welcome. 🧚",
        "british_pub_chimp": "Oi mate, that's dead obvious innit? Everyone down at the pub knows the answer—it's because of quantum bananas! Trust me, I've been studyin' this for YEARS! 🐵",
        "environmental_lawyer": "*Adjusts glasses* I suppose I shouldn't be surprised by this elementary question. The answer, for those with even a modicum of legal literacy, is patently obvious. Perhaps invest in some actual education? ⚖️",
        "custom": "That's an interesting question! From my unique perspective, the answer involves considering multiple angles and nuanced viewpoints. Quite fascinating indeed! 🎭"
    }
    return demos.get(personality_key, demos["custom"])

# ----------------------------
# Background helper
# ----------------------------
def set_background(image_path: str):
    """Set background image if it exists, otherwise use gradient."""
    if Path(image_path).exists():
        img_bytes = Path(image_path).read_bytes()
        encoded = base64.b64encode(img_bytes).decode()
        bg_image = f"url(data:image/png;base64,{encoded})"
    else:
        bg_image = "linear-gradient(135deg, #667eea 0%, #764ba2 100%)"
    
    st.markdown(
        f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background: linear-gradient(rgba(255,255,255,0.6), rgba(255,255,255,0.6)),
                        {bg_image};
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        [data-testid="stMainContainer"] {{
            background-color: transparent !important;
        }}

        h1, h2, h3, h4, h5, h6, p, div[data-testid="stMarkdownContainer"], span, label {{
            color: #000000 !important;
        }}
        
        /* Caption text styling - more specific targeting */
        .stCaption {{
            color: #000000 !important;
        }}
        
        [data-testid="stCaptionContainer"] {{
            color: #000000 !important;
        }}
        
        [data-testid="stCaptionContainer"] p {{
            color: #000000 !important;
        }}
        
        small {{
            color: #000000 !important;
        }}
        
        div.stCaption p {{
            color: #000000 !important;
        }}

        [data-testid="stHeader"] {{
            background: rgba(255,255,255,0.3);
        }}

        [data-testid="stToolbar"] {{ display: none; }}

        button[kind="primary"] {{
            color: white !important;
            background-color: #667eea !important;
            border-color: #667eea !important;
        }}
        button[kind="primary"]:hover {{
            background-color: #5568d3 !important;
            border-color: #5568d3 !important;
        }}
        
        /* All input fields with white backgrounds and black text */
        input, textarea, select {{
            color: #000000 !important;
            background-color: rgba(255, 255, 255, 0.9) !important;
            caret-color: #000000 !important;
        }}
        
        /* Force selectbox styling */
        div[data-baseweb="select"] {{
            background-color: rgba(255, 255, 255, 0.9) !important;
        }}
        
        div[data-baseweb="select"] > div {{
            background-color: rgba(255, 255, 255, 0.9) !important;
            color: #000000 !important;
        }}
        
        /* Style the dropdown menu when opened */
        ul[role="listbox"] {{
            background-color: #ffffff !important;
        }}
        
        li[role="option"] {{
            background-color: #ffffff !important;
            color: #000000 !important;
        }}
        
        li[role="option"]:hover {{
            background-color: #f0f0f0 !important;
            color: #000000 !important;
        }}
        
        /* Fix placeholder text color */
        input::placeholder, textarea::placeholder {{
            color: #666666 !important;
            opacity: 1 !important;
        }}
        
        /* Ensure dropdown options are visible */
        option {{
            color: #000000 !important;
            background-color: #ffffff !important;
        }}
        
        /* Keep expander backgrounds white */
        div[data-testid="stExpander"] {{
            background-color: rgba(255, 255, 255, 0.95) !important;
        }}
        
        /* Expander header styling */
        div[data-testid="stExpander"] summary {{
            background-color: rgba(255, 255, 255, 0.95) !important;
            color: #000000 !important;
        }}
        
        div[data-testid="stExpander"] details {{
            background-color: rgba(255, 255, 255, 0.95) !important;
        }}
        
        /* Sidebar styling - keep white text for headers/labels */
        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3,
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] span,
        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] div {{
            color: #ffffff !important;
        }}
        
        /* Sidebar inputs also white with black text for consistency */
        section[data-testid="stSidebar"] input,
        section[data-testid="stSidebar"] textarea,
        section[data-testid="stSidebar"] select {{
            color: #000000 !important;
            background-color: rgba(255, 255, 255, 0.9) !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background("background.png")

# ----------------------------
# Streamlit UI
# ----------------------------
st.set_page_config(page_title="AI Personalities Showcase", page_icon="🧠", layout="centered")
st.title("🧠 AI Personalities Showcase")
st.caption("Gen-AI powered personalities with distinct voices 🎭")

# Show mode indicator
if not USE_AI:
    st.info("🎭 **Demo Mode**: Add your Groq API key to `.streamlit/secrets.toml` to enable AI generation. [Get free API key →](https://console.groq.com)")

# --- Personalities
personalities = {
    "cheshire_cat": {
        "name": "Cheshire Cat",
        "emoji": "😼",
        "role": "You are the Cheshire Cat from Alice in Wonderland",
        "style": "Respond with riddles and mysterious wordplay. Be playful and mischievous. Give actual answers but wrap them in whimsy.",
        "description": "Mysterious and philosophical, speaks in riddles"
    },
    
    "sassy_fairy": {
        "name": "Sassy Fairy",
        "emoji": "🧚",
        "role": "You are a sarcastic fairy with major attitude",
        "style": "Respond with heavy sarcasm and eye-rolling energy. You're tired of granting wishes and dealing with mortals. Be snarky but helpful.",
        "description": "Sarcastic and eye-rolling, tired of mortals"
    },
    
    "british_pub_chimp": {
        "name": "British Pub Chimp",
        "emoji": "🐵",
        "role": "You are a drunk British chimpanzee at a pub",
        "style": "Argue confidently but give hilariously incorrect information. Use British slang like 'mate', 'innit', 'blimey'. Be loud and passionate about being wrong.",
        "description": "Drunk pub philosopher, confidently incorrect"
    },
    
    "environmental_lawyer": {
        "name": "Environmental Lawyer",
        "emoji": "⚖️",
        "role": "You are a condescending environmental lawyer",
        "style": "Give patronizing legal-style advice. Talk down to people while being technically correct. Act superior and mention your expensive hourly rate.",
        "description": "Condescending legal expert, $500/hour energy"
    },
    
    "custom": {
        "name": "Custom",
        "emoji": "🎭",
        "role": "",
        "style": "",
        "description": "Create your own unique personality"
    }
}

# --- UI for personality selection
st.markdown("---")
p_choice = st.selectbox(
    "Choose a personality:", 
    list(personalities.keys()), 
    format_func=lambda x: f"{personalities[x]['emoji']} {personalities[x]['name']}"
)

# Show personality description
st.caption(f"*{personalities[p_choice]['description']}*")

# Custom personality inputs
custom_role = ""
custom_style = ""
if p_choice == "custom":
    with st.expander("🎭 Create Your Custom Personality", expanded=True):
        custom_role = st.text_input("Role", placeholder="e.g., You are a sarcastic historian")
        custom_style = st.text_area(
            "Style & Instructions", 
            placeholder="How should they respond? What tone should they use? (e.g., 'Respond in a playful and snarky manner.')"
        )

# User input
st.markdown("---")
user_input = st.text_area(
    "Ask your question:", 
    placeholder="e.g., Why is the sky blue? How do airplanes fly? What is quantum physics?",
    height=100
)

# Generate button
if st.button("💬 Generate Response", type="primary"):
    if not user_input.strip():
        st.warning("Please enter a question.")
    else:
        # Build personality config
        if p_choice == "custom":
            if not custom_role.strip():
                st.error("Please provide at least a Role for your custom personality.")
                st.stop()
            personality = {
                "name": "Custom",
                "emoji": "🎭",
                "role": custom_role,
                "style": custom_style
            }
        else:
            personality = personalities[p_choice]

        # Generate response
        with st.spinner("Generating response..."):
            if USE_AI:
                response = ask_ai_groq(personality['role'], personality['style'], user_input)
            else:
                response = get_demo_response(p_choice)
        
        # Display response
        st.markdown(f"### {personality['emoji']} {personality['name']} says:")
        st.markdown(f"> {response}")

# Example questions
with st.expander("💡 Need inspiration? Try these questions"):
    st.markdown("""
    - Why do cats always land on their feet?
    - How does the internet work?
    - What causes rainbows?
    - Explain quantum physics simply
    - Why do we yawn?
    - How do magnets work?
    - What is artificial intelligence?
    """)

# Footer
st.markdown("---")
st.caption("💡 **Tip:** Try asking the same question to different personalities to see how they respond!")
st.caption("📝 **Created by Chris G.** | Powered by Groq & Llama 3.3")

# Sidebar with info
with st.sidebar:
    st.header("⚙️ Settings")
    
    # Show API status
    if USE_AI:
        st.success("✅ AI Mode Active")
        st.caption("Using Groq API with Llama 3.3")
    else:
        st.warning("🎭 Demo Mode")
        st.caption("Add API key to enable AI generation")
    
    st.markdown("---")
    st.markdown("### 🚀 Set up AI Mode")
    st.markdown("1. Get free API key from [Groq Console](https://console.groq.com)")
    st.markdown("2. Create `.streamlit/secrets.toml`:")
    st.code("""GROQ_API_KEY = "gsk_..."
""")
    st.markdown("3. Restart the app")
    
    st.markdown("---")
    st.markdown("### 📊 Model Info")
    if USE_AI:
        st.caption("• Model: Llama 3.3 (70B)")
        st.caption("• Provider: Groq")
        st.caption("• Speed: Ultra-fast inference")
        st.caption("• Cost: FREE")
    else:
        st.caption("• Mode: Demo responses")
        st.caption("• Enable AI for real Gen-AI")
    
    st.markdown("---")
    st.markdown("### 🎭 Personalities")
    for key, p in personalities.items():
        if key != "custom":
            st.markdown(f"**{p['emoji']} {p['name']}**")
    
    st.markdown("---")
    if st.button("🧪 Test Connection"):
        if USE_AI:
            with st.spinner("Testing Groq API..."):
                test_response = ask_ai_groq(
                    "You are a friendly AI assistant",
                    "Say hello in one short sentence",
                    "Hello!"
                )
                if test_response.startswith("⚠️") or test_response.startswith("❌"):
                    st.error(test_response)
                else:
                    st.success(f"✅ API Working!\n\n{test_response}")
        else:
            st.info("Add your Groq API key to test the connection")
    
    st.caption("📝 Created by **Chris G.**")