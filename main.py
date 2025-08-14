import streamlit as st
import random

st.set_page_config(page_title="재미있는 MBTI 테스트", page_icon="😆", layout="centered")

# --------------------------
# MBTI 데이터
# --------------------------
mbti_info = {
    "INTJ": {"nickname": "전략 천재", "jobs": ["데이터 과학자", "경영 컨설턴트", "연구원"], "img": "https://picsum.photos/seed/intj/400/300"},
    "ENTP": {"nickname": "아이디어 폭탄", "jobs": ["광고 기획자", "창업가", "마케터"], "img": "https://picsum.photos/seed/entp/400/300"},
    "ENFP": {"nickname": "불타는 모험가", "jobs": ["유튜버", "이벤트 플래너", "여행 작가"], "img": "https://picsum.photos/seed/enfp/400/300"},
    "ISTJ": {"nickname": "원칙주의자", "jobs": ["회계사", "공무원", "품질관리자"], "img": "https://picsum.photos/seed/istj/400/300"},
    # 필요하면 16개 전부 추가 가능
}

# --------------------------
# 질문 데이터
# --------------------------
questions = [
    ("사람 많은 파티에 가는 것을 좋아한다.", "E", "I"),
    ("즉흥적인 결정을 잘 내린다.", "P", "J"),
    ("감정보다 논리를 중시한다.", "T", "F"),
    ("새로운 아이디어를 떠올리는 걸 즐긴다.", "N", "S"),
    ("친구를 사귀는 게 어렵지 않다.", "E", "I"),
    ("계획대로 움직이는 걸 좋아한다.", "J", "P"),
    ("사람들의 감정을 잘 읽는다.", "F", "T"),
    ("현실보다는 가능성을 더 본다.", "N", "S"),
]

# --------------------------
# 세션 상태 초기화
# --------------------------
if "page" not in st.session_state:
    st.session_state.page = "quiz"
if "answers" not in st.session_state:
    st.session_state.answers = []

# --------------------------
# 퀴즈 페이지
# --------------------------
if st.session_state.page == "quiz":
    st.title("😆 재미있는 MBTI 미니 테스트")
    st.caption("8문항으로 가볍게 즐기는 MBTI 테스트")
    
    st.session_state.answers = []
    for q, a1, a2 in questions:
        ans = st.radio(q, [a1, a2], index=None, horizontal=True)
        st.session_state.answers.append(ans)
    
    if None not in st.session_state.answers:
        if st.button("결과 보기"):
            st.session_state.page = "result"
            st.experimental_rerun()

# --------------------------
# 결과 페이지
# --------------------------
elif st.session_state.page == "result":
    # 각 글자 빈도 계산
    counts = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
    for ans in st.session_state.answers:
        counts[ans] += 1

    mbti_type = (
        ("E" if counts["E"] >= counts["I"] else "I") +
        ("S" if counts["S"] >= counts["N"] else "N") +
        ("T" if counts["T"] >= counts["F"] else "F") +
        ("J" if counts["J"] >= counts["P"] else "P")
    )

    st.title(f"당신의 MBTI는 **{mbti_type}** 🎉")
    
    if mbti_type in mbti_info:
        info = mbti_info[mbti_type]
        st.subheader(f"별명: {info['nickname']}")
        st.image(info["img"])
        st.markdown("### 추천 직업")
        for job in info["jobs"]:
            st.write(f"- {job}")
    else:
        st.warning("이 MBTI 유형에 대한 데이터가 없습니다. 😅")

    if st.button("다시 테스트하기"):
        st.session_state.page = "quiz"
        st.experimental_rerun()
