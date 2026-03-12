import streamlit as st
import base64

def get_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

bg = get_base64("background.jpg")

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{bg}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
import streamlit as st
import random

st.set_page_config(page_title="Ticket Site", page_icon="🎤")

st.title("🎤 Билети за концерт на Емануела")

st.write("Купи билет за най-легендарния концерт на годината!")

name = st.text_input("👤 Въведи име")

date = st.selectbox(
    "📅 Избери дата",
    ["12 юли", "18 юли", "25 юли"]
)

ticket = st.selectbox(
    "🎟️ Тип билет",
    ["Стандартен – 40лв", "VIP – 120лв", "Ultra VIP – 500лв"]
)

extras = st.multiselect(
    "🔥 VIP екстри",
    ["Селфи с Емануела", "Безплатно питие", "Кючек зона", "Backstage достъп"]
)

rating = st.slider("⭐ Колко очакваш да е як концертът?", 1, 10)

tickets = st.number_input("🎫 Брой билети", 1, 10)

if st.button("Купи билет"):
    
    jokes = [
        "Билетът е запазен! Плаща се с 2 водки.",
        "VIP билетите свършиха... защото Кекса купи всички.",
        "Системата засече прекалено много кючек енергия.",
        "Успешно! Но това е майтап сайт 😄"
        "Баклавички приятен концерт!!!"
    ]

    st.success(f"Благодаря, {name}! Резервира {tickets} билет(а).")
    st.write("Дата:", date)
    st.write("Тип билет:", ticket)
    st.write("Екстри:", extras)
    
    st.info(random.choice(jokes))
    
    st.balloons()
