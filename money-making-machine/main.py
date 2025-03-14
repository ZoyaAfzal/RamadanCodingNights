'''import streamlit as st
import random
import time
import requests

st.title("Money Making Machine")

def generate_money():
    return random.randint(1, 1000)

st.subheader("Instant Cash Generator")
if st.button("Generate Money"):
    st.write("Counting your money...")
    time.sleep(1)
    amount = generate_money()
    st.success(f"You made ${amount}")


def fetch_side_hustle():
    try:
        response = requests.get("http://127.0.0.1:8000/side-hustles?api_key=1234567890")
        if response.status_code == 200:
            hustles = response.json()
            return hustles["side_hustle"]
        else:
            return("Freelancing")
    except:
        return("Something went wrong!")
    
st.subheader("Side Hustle Ideas")
if st.button("Generate Hustle"):
    idea = fetch_side_hustle()
    st.success(idea)

def fetch_money_quote():
    try:
        response = requests.get("http://127.0.0.1:8000/money-quotes?api_key=1234567890")
        if response.status_code == 200:
            quotes = response.json()
            return quotes["money_quote"]
        else:
            return("Money is the root of all evil.")
    except:
        return("Something went wrong!")
    
st.subheader("Money-Making Motivation")
if st.button("Get Inspired"):
    quote = fetch_money_quote()
    st.info(quote)
'''

import streamlit as st
import random
import time
import requests

# Page configuration with dark mode
st.set_page_config(page_title="Money Making Machine", layout="centered")
st.markdown(
    """
    <style>
    body {
        color: #f5f5f5;
        background-color: #0e1117;
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
        response = requests.get("http://127.0.0.1:8000/side-hustles?api_key=1234567890")
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
        response = requests.get("http://127.0.0.1:8000/money-quotes?api_key=1234567890")
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

