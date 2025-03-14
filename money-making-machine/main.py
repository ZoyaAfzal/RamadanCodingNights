import streamlit as st
import random
import time
import requests

# Page configuration with dark mode
st.set_page_config(page_title="Money Making Machine", layout="centered")
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0e1117 !important;
        color:white
    }
     /* Make all text white */
    * {
        color: white !important;
    }

    /* Target all text inside the app */
    .main * {
        color: #f5f5f5 !important;
    }
      /* Navbar background color */
    header[data-testid="stHeader"] {
        background-color: #1a1d23 !important; 
    }

    /* Styling for success alert */
    .stAlert[data-baseweb="alert"][kind="success"] {
        background-color: #1e7e34 !important;
        color: white !important;
        border-radius: 10px;
        padding: 10px;
    }

    /* Styling for info alert */
    .stAlert[data-baseweb="alert"][kind="info"] {
        background-color: #0275d8 !important;
        color: white !important;
        border-radius: 10px;
        padding: 10px;
    }

    .stButton>button {
        background-color: #ff9800 !important;
        color: white !important;
        font-size: 16px;
        padding: 10px;
        border-radius: 10px;
    }
    .stButton>button:hover {
        background-color: #f57c00 !important;
    }
    .stAlert {
        background-color: #212121 !important;
    }
        /* Styling for error message */
    .stAlert[data-baseweb="alert"][kind="error"] {
        background-color: #d9534f !important;
        color: white !important;
        border-radius: 10px;
        padding: 10px;
        font-weight: bold;
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.title("💰 Money Making Machine 💸")

# Money generator function
def generate_money():
    return random.randint(1, 1000)

st.subheader("🤑 Instant Cash Generator")
if st.button("Generate Money 💵"):
    with st.spinner("Counting your money... 💰"):
        time.sleep(2)
    amount = generate_money()
    st.success(f"🎉 You made **${amount}**!")

# Fetch Side Hustle ideas from API
def fetch_side_hustle():
    try:
        response = requests.get("https://fastapi-api.vercel.app/side_hustles")
        if response.status_code == 200:
            hustles = response.json()
            return hustles["side_hustle"]
        else:
            return "Freelancing"
    except:
        return "⚠️ Something went wrong!"

st.subheader("🚀 Side Hustle Ideas")
if st.button("Generate Hustle 💡"):
    idea = fetch_side_hustle()
    st.success(f" {idea}")

# Fetch Money Motivation Quotes
def fetch_money_quote():
    try:
        response = requests.get("https://fastapi-api.vercel.app/money_quotes")
        if response.status_code == 200:
            quotes = response.json()
            return quotes["money_quote"]
        else:
            return "💵 'Money is the root of all evil.'"
    except:
        return "⚠️ Something went wrong!"

st.subheader("💪 Money-Making Motivation")
if st.button("Get Inspired ✨"):
    quote = fetch_money_quote()
    st.info(f"💬 *{quote}*")

# Footer
st.markdown("---")
st.markdown("*Developed by ❤️ Zoya Afzal*")

