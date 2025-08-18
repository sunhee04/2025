import streamlit as st
import datetime
import random

st.title("오늘의 운세 & 시험 점수 예측기 🎉")

# 이름 입력
name = st.text_input("이름을 입력하세요")

# 생년월일 입력 (1900년 ~ 2035년)
birthdate = st.date_input(
    "생년월일을 선택하세요",
    min_value=datetime.date(1900, 1, 1),
    max_value=datetime.date(2035, 12, 31),
)

# 오늘의 기분 입력
mood = st.text_input("오늘의 기분을 한 단어로 표현한다면?")

# 버튼 클릭 시 운세 및 점수 출력
if st.button("🔮 운세 보기"):
    if name and mood:
        fortunes = [
            "길운이 가득한 하루! 🍀",
            "조심해서 다녀야 할 하루 😬",
            "뜻밖의 행운이 찾아올 예정입니다 ✨",
            "평범하지만 소소한 행복이 있는 하루 ☺️",
            "행운과 불운이 50:50으로 섞인 하루 🤔"
        ]

        exam_scores = [
            "100점 만점 중 **100점**?! 선생님도 놀랄 실력!",
            "오늘은 **72점** 정도! 그래도 기분 좋게 🍰",
            "그냥 **50점** 넘으면 다행인 날 😅",
            "믿기 어렵겠지만 **98점** 예상됩니다 🔥",
            "점수가 중요한 게 아니야… **마음가짐**이 중요하지 😇"
        ]

        st.subheader(f"✨ {name}님의 오늘의 운세")
        st.write(random.choice(fortunes))

        st.subheader("🧠 오늘의 시험 점수 예측")
        st.write(random.choice(exam_scores))

        st.write(f"현재 기분인 **{mood}**(으)로 시작한 오늘, 멋진 하루 보내세요!")
    else:
        st.warning("이름과 기분을 모두 입력해주세요.")
