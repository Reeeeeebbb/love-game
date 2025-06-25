import streamlit as st
import random

# Title
st.set_page_config(page_title="Areeb & Zoya", page_icon="💘"), layout="centered")
st.title("💞 Zoya & Areeb Forever 💞")

# Pyar bhare messages
love_messages = [
    "Aap meri duniya hein💖",
    "Aapka hona sabse khoobsurat ehsaas hai ✨",
    "Main aapse har din aur zyada pyar karta hoon 😘",
    "Aapke bina sab kuch suna suna lagta hai 🥺",
    "Aapka naam sochke hi muskurahat aa jaati hai 😊"
]

# Cute tasks
love_tasks = [
    "Abhi ek 'I Love You' message bhejo ❤️",
    "Apni fav memory type karo 💬",
    "Ek choti si poem likho uske liye ✍️",
    "Uske future naam ka signature banake bhejo 😂",
    "Ek sweet photo uske saath share karo 📸"
]

st.markdown("### Pyar se ek option chuno:")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("💌 Love Message"):
        st.success(random.choice(love_messages))

with col2:
    if st.button("🎲 Cute Task"):
        st.info(random.choice(love_tasks))

with col3:
    if st.button("🔄 Reset"):
        st.warning("💘 Pyar se kuch choose karo upar se 💘")

st.markdown("---")
st.caption("Made with ❤️ by Areeb, for Zoya 💍")