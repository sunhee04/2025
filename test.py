import streamlit as st

st.title("Daily Fortune & Exam Score Predictor")

name = st.text_input("Enter your name:")
birth = st.date_input("Enter your birth date:", min_value=datetime.date(1800,1,1), max_value=datetime.date(2035,12,31))
mood = st.selectbox("How do you feel today?", ["😄 Happy", "😐 Okay", "😢 Sad", "😡 Angry", "😴 Tired"])

if st.button("Get My Fortune!"):
    import random
    fortunes = [
        "Today is a perfect day to try something new!",
        "Beware of unexpected quizzes... but you will ace them!",
        "Luck will find you when you least expect it.",
        "Someone will buy you coffee today. Probably." ,
        "Your internet connection will be faster than ever today."
    ]
    score_prediction = random.randint(40,100)
    st.subheader(f"🧠 Fortune for {name}")
    st.write(random.choice(fortunes))
    st.subheader("📚 Predicted Exam Score")
    st.write(f"Your next exam score will be... **{score_prediction}** out of 100! 😆")
