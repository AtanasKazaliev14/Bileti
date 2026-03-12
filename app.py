import streamlit as st
import random

st.set_page_config(page_title="Ticket Site", page_icon="🎤", layout="wide")

# --- ФОН ---
background_url = "https://images.unsplash.com/photo-1492684223066-81342ee5ff30"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{background_url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color: #ffffff;  /* бял цвят на текста */
    }}

    /* леко тъмен слой за по-добра четимост на бял текст */
    .stApp::before {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0,0,0,0.3);
        z-index: -1;
    }}

    /* смяна на цвета на заглавия, текст и labels */
    h1, h2, h3, h4, h5, h6, p, label, div {{
        color: #ffffff !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- СЪДЪРЖАНИЕ ---
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
        "Успешно! Но това е майтап сайт 😄",
        "Баклавички приятен концерт!!!"
    ]

    st.success(f"Благодаря, {name}! Резервира {tickets} билет(а).")
    st.write("Дата:", date)
    st.write("Тип билет:", ticket)
    st.write("Екстри:", extras)
   
    st.info(random.choice(jokes))
   
    st.balloons()
