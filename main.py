import streamlit as st
import random

st.set_page_config(page_title="MBTI 음식 추천", page_icon="🍜", layout="centered")

# --------------------------
# 16개 MBTI 음식 데이터
# --------------------------
food_data = {
    "ENFP": [
        {"name": "타코 🌮", "desc": "당신처럼 자유롭고 화려한 맛!"},
        {"name": "망고 빙수 🍧", "desc": "시원하고 달콤한 당신에게 딱!"}
    ],
    "ENTP": [
        {"name": "핫도그 🌭", "desc": "아이디어처럼 휘리릭 만들 수 있는 간식!"},
        {"name": "불닭볶음면 🔥", "desc": "도전 정신을 불태우는 매운맛!"}
    ],
    "ENFJ": [
        {"name": "샐러드 🥗", "desc": "모두를 챙기는 따뜻한 마음처럼 건강한 맛"},
        {"name": "치즈케이크 🍰", "desc": "부드럽고 달콤하게 사람을 사로잡는 맛"}
    ],
    "ENTJ": [
        {"name": "스테이크 🥩", "desc": "강한 추진력처럼 묵직한 맛"},
        {"name": "에스프레소 ☕", "desc": "짧고 강렬한 리더십의 맛"}
    ],
    "INFJ": [
        {"name": "허브티 🍵", "desc": "조용히 마음을 달래주는 따뜻함", "img": "https://picsum.photos/seed/infj1/400/300"},
        {"name": "초콜릿 🍫", "desc": "깊고 달콤한 매력", "img": "https://picsum.photos/seed/infj2/400/300"}
    ],
    "INFP": [
        {"name": "마카롱 🥮", "desc": "감성적인 색감과 부드러운 맛", "img": "https://picsum.photos/seed/infp1/400/300"},
        {"name": "허니브레드 🍯", "desc": "따뜻하고 달달한 위로", "img": "https://picsum.photos/seed/infp2/400/300"}
    ],
    "INTJ": [
        {"name": "다크 초콜릿 🍫", "desc": "깊이 있는 전략가의 맛", "img": "https://picsum.photos/seed/intj1/400/300"},
        {"name": "와인 🍷", "desc": "품격 있는 선택", "img": "https://picsum.photos/seed/intj2/400/300"}
    ],
    "INTP": [
        {"name": "마라탕 🌶", "desc": "복잡하지만 매력적인 조합", "img": "https://picsum.photos/seed/intp1/400/300"},
        {"name": "아메리카노 ☕", "desc": "쓴맛 속 깊은 향기", "img": "https://picsum.photos/seed/intp2/400/300"}
    ],
    "ESFP": [
        {"name": "치즈피자 🍕", "desc": "모든 순간을 즐기는 당신의 필수 메뉴", "img": "https://picsum.photos/seed/esfp1/400/300"},
        {"name": "아이스크림 🍦", "desc": "달콤하고 시원한 에너지", "img": "https://picsum.photos/seed/esfp2/400/300"}
    ],
    "ESTP": [
        {"name": "치킨 🍗", "desc": "활발하고 대담한 당신에게 딱", "img": "https://picsum.photos/seed/estp1/400/300"},
        {"name": "버거 🍔", "desc": "즉흥적인 모험처럼 빠른 한 끼", "img": "https://picsum.photos/seed/estp2/400/300"}
    ],
    "ESFJ": [
        {"name": "파스타 🍝", "desc": "부드럽고 친근한 관계를 닮은 맛", "img": "https://picsum.photos/seed/esfj1/400/300"},
        {"name": "팬케이크 🥞", "desc": "따뜻하게 사람을 감싸는 달콤함", "img": "https://picsum.photos/seed/esfj2/400/300"}
    ],
    "ESTJ": [
        {"name": "돈까스 🍖", "desc": "바삭하고 단정한 맛", "img": "https://picsum.photos/seed/estj1/400/300"},
        {"name": "김밥 🍙", "desc": "체계적으로 완벽하게 말아낸 맛", "img": "https://picsum.photos/seed/estj2/400/300"}
    ],
    "ISFP": [
        {"name": "크로와상 🥐", "desc": "예술적인 결을 가진 부드러움", "img": "https://picsum.photos/seed/isfp1/400/300"},
        {"name": "티라미수 🍮", "desc": "은은하게 매혹적인 단맛", "img": "https://picsum.photos/seed/isfp2/400/300"}
    ],
    "ISTP": [
        {"name": "라면 🍜", "desc": "간단하지만 중독적인 맛", "img": "https://picsum.photos/seed/istp1/400/300"},
        {"name": "스시 🍣", "desc": "정교하게 완성된 한 입", "img": "https://picsum.photos/seed/istp2/400/300"}
    ],
    "ISFJ": [
        {"name": "죽 🍚", "desc": "포근하고 편안하게 감싸주는 맛", "img": "https://picsum.photos/seed/isfj1/400/300"},
        {"name": "쿠키 🍪", "desc": "언제나 반가운 달콤함", "img": "https://picsum.photos/seed/isfj2/400/300"}
    ],
    "ISTJ": [
        {"name": "된장찌개 🍲", "desc": "전통과 안정감의 상징", "img": "https://picsum.photos/seed/istj1/400/300"},
        {"name": "군만두 🥟", "desc": "깔끔하고 담백한 스타일", "img": "https://picsum.photos/seed/istj2/400/300"}
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
