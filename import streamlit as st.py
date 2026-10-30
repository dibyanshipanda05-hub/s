import streamlit as st
import time

# Page Configuration
st.set_page_config(page_title="For You, My Love", page_icon="🌹", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #fff0f3;
    }
    .stButton>button {
        background-color: #ff4d6d;
        color: white;
        font-size: 18px;
        border-radius: 20px;
        padding: 10px 25px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #c9184a;
        color: white;
    }
    .title-text {
        color: #800f2f;
        text-align: center;
        font-family: 'Georgia', serif;
    }
    </style>
""", unsafe_allow_html=True)

# Application UI
st.markdown("<h1 class='title-text'>🌹 A Flower For You 🌹</h1>", unsafe_allow_html=True)
st.write("---")

st.image("https://images.unsplash.com/photo-1518709268805-4e9042af9f23?q=80&w=800", caption="Just for you ❤️", use_column_width=True)

st.markdown("""
### My Dearest,
Every single day with you feels like a bloom in spring.  
Thank you for bringing so much happiness, warmth, and warmth into my life!

**I love you infinitely! ❤️**
""")

# Interactive button
if st.button("Click for a Surprise 💖"):
    st.balloons()
    st.success("You are my favorite person in the entire universe! 🥰")