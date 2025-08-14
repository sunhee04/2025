import streamlit as st
import random

st.set_page_config(page_title="MBTI 음식 추천", page_icon="🍜", layout="centered")

# --------------------------
# 데이터
# --------------------------
food_data = {
    "ENFP": [
        {"name": "타코 🌮", "desc": "당신처럼 자유롭고 화려한 맛!", "img": "https://picsum.photos/seed/taco/400/300"},
        {"name": "망고 빙수 🍧", "desc": "시원하고 달콤한 당신에게 딱!", "img": "https://picsum.photos/seed/mango/400/300"}
    ],
    "ISTJ": [
        {"name": "된장찌개 🍲", "desc": "전통과 안정감의 상징", "img": "https://picsum.photos/seed/soy/400/300"},
        {"name": "군만두 🥟", "desc": "깔끔하고 담백한 스타일", "img": "https://picsum.photos/seed/dumpling/400/300"}
    ],
    "INTP": [
        {"name": "마라탕 🌶", "desc": "복잡한 조합, 그러나 매력적!", "img": "https://picsum.photos/seed/mala/400/300"},
        {"name": "아메리카노 ☕", "desc": "쓴맛 속 깊은 향기", "img": "https://picsum.photos/seed/coffee/400/300"}
    ]
}

all_foods = [food for foods in food_data.values() for food in foods]

# --------------------------
# UI
# --------------------------
st.title("🍜 MBTI 음식 추천")
st.caption("당신의 MBTI에 어울리는 음식과 디저트를 찾아드립니다.")

mbti = st.selectbox("MBTI를 선택하세요:", list(food_data.keys()))
random_mode = st.checkbox("엉뚱한 랜덤 추천 받기 🎲")

if st.button("추천 보기"):
    if random_mode:
        choice = random.choice(all_foods)
    else:
        choice = random.choice(food_data[mbti])
    
    st.image(choice["img"], caption=choice["name"])
    st.subheader(choice["name"])
    st.write(choice["desc"])
