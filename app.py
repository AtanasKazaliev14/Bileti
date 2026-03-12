import streamlit as st

st.title("🎤 Билети за концерт на Емануела")

name = st.text_input("Име")

date = st.selectbox(
    "Избери дата",
    ["12 юли", "18 юли", "25 юли"]
)

ticket_type = st.selectbox(
    "Тип билет",
    ["Стандартен – 40лв", "VIP – 120лв", "Ultra VIP – 500лв"]
)

count = st.number_input("Брой билети", min_value=1, max_value=10)

if st.button("Купи билет"):
    st.success(f"{name}, билетът е резервиран!")
    st.info("НЕ Е МАЙТАП")
