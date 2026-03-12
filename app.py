bg_url = "https://www.google.com/search?sca_esv=f5b8765b7b50f1bf&udm=2&fbs=ADc_l-aN0CWEZBOHjofHoaMMDiKpaEWjvZ2Py1XXV8d8KvlI3jljrY5CkLlk8Dq3IvwBz-SJyfRX_inP-J3Cs9lQZu9J-w-s39WMlkYCuZrBZDnSTW7OXuSDEQSVLUzfyzqI1jWpENUC4uWpCIdxdmLCQnvNttnwC5mQyhzLnniQQw33yXpl3w0&q=%D0%B0%D1%80%D0%B5%D0%BD%D0%B0+8888&sa=X&ved=2ahUKEwinsomB3JmTAxWthf0HHcZZBSMQtKgLegQIEhAB&biw=1536&bih=738&dpr=1.25#sv=CAMSVhoyKhBlLXFzanRtM2NKc21lRFBNMg5xc2p0bTNjSnNtZURQTToOU2RwTEppRUIxb3owY00gBCocCgZtb3NhaWMSEGUtcXNqdG0zY0pzbWVEUE0YADABGAcgg9z_zgEwAkoIEAIYAiACKAI"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{bg_url}");
        background-size: cover;
        background-position: center;
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
