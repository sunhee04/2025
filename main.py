# app.py (MBTI 16개 + 검색 + 안정적 이미지 표시)
# 이미지: picsum.photos의 시드 기반 정적 URL을 사용해 항상 로딩되도록 구성
#   - 예) https://picsum.photos/seed/ISTJ-회계사/800/500
#   - 같은 시드에 대해 언제나 같은 이미지를 반환합니다(안정적 표시 목적)

import urllib.parse
import streamlit as st
from typing import List, Dict

st.set_page_config(page_title="MBTI 기반 진로 추천", page_icon="💼", layout="wide")

# ------------------------------------------------------------
# 데이터: 16개 MBTI × 5개 직업
# ------------------------------------------------------------
MBTI_JOBS: Dict[str, List[Dict[str, str]]] = {
    "ISTJ": [
        {"job": "회계사"},
        {"job": "데이터 분석가"},
        {"job": "군인"},
        {"job": "품질관리 엔지니어"},
        {"job": "행정 공무원"},
    ],
    "ISFJ": [
        {"job": "간호사"},
        {"job": "초등교사"},
        {"job": "사회복지사"},
        {"job": "비서"},
        {"job": "심리상담사"},
    ],
    "INFJ": [
        {"job": "심리학자"},
        {"job": "작가"},
        {"job": "교육 컨설턴트"},
        {"job": "사회운동가"},
        {"job": "예술가"},
    ],
    "INTJ": [
        {"job": "전략기획가"},
        {"job": "데이터 사이언티스트"},
        {"job": "연구원"},
        {"job": "경영 컨설턴트"},
        {"job": "시스템 엔지니어"},
    ],
    "ISTP": [
        {"job": "정비사"},
        {"job": "파일럿"},
        {"job": "소방관"},
        {"job": "경찰관"},
        {"job": "응급구조사"},
    ],
    "ISFP": [
        {"job": "패션 디자이너"},
        {"job": "사진작가"},
        {"job": "요리사"},
        {"job": "음악가"},
        {"job": "실내디자이너"},
    ],
    "INFP": [
        {"job": "작가"},
        {"job": "상담가"},
        {"job": "번역가"},
        {"job": "비영리단체 활동가"},
        {"job": "콘텐츠 기획자"},
    ],
    "INTP": [
        {"job": "연구원"},
        {"job": "프로그래머"},
        {"job": "과학자"},
        {"job": "발명가"},
        {"job": "데이터 분석가"},
    ],
    "ESTP": [
        {"job": "영업 전문가"},
        {"job": "기업가"},
        {"job": "스포츠 코치"},
        {"job": "마케팅 전문가"},
        {"job": "이벤트 기획자"},
    ],
    "ESFP": [
        {"job": "배우"},
        {"job": "가수"},
        {"job": "여행 가이드"},
        {"job": "MC"},
        {"job": "영업 매니저"},
    ],
    "ENFP": [
        {"job": "광고 기획자"},
        {"job": "홍보 전문가"},
        {"job": "작가"},
        {"job": "심리 상담가"},
        {"job": "이벤트 플래너"},
    ],
    "ENTP": [
        {"job": "기업가"},
        {"job": "마케팅 디렉터"},
        {"job": "변호사"},
        {"job": "벤처 투자자"},
        {"job": "기술 혁신가"},
    ],
    "ESTJ": [
        {"job": "프로젝트 매니저"},
        {"job": "경영자"},
        {"job": "군 간부"},
        {"job": "행정관리자"},
        {"job": "영업 관리자"},
    ],
    "ESFJ": [
        {"job": "간호사"},
        {"job": "교사"},
        {"job": "HR 매니저"},
        {"job": "상담사"},
        {"job": "영양사"},
    ],
    "ENFJ": [
        {"job": "교육자"},
        {"job": "리더십 코치"},
        {"job": "사회운동가"},
        {"job": "심리상담사"},
        {"job": "홍보 전문가"},
    ],
    "ENTJ": [
        {"job": "경영 컨설턴트"},
        {"job": "CEO"},
        {"job": "변호사"},
        {"job": "프로젝트 디렉터"},
        {"job": "마케팅 전략가"},
    ],
}

# ------------------------------------------------------------
# 유틸: 직업명과 MBTI를 시드로 사용해 '항상 표시되는' 이미지 URL 생성
# ------------------------------------------------------------

def img_url(mbti: str, job: str, w: int = 800, h: int = 500) -> str:
    seed = f"{mbti}-{job}"
    return f"https://picsum.photos/seed/{urllib.parse.quote(seed)}/{w}/{h}"


def normalize(s: str) -> str:
    return "".join(s.lower().split())


def filter_jobs(keyword: str):
    k = normalize(keyword)
    results = []
    for t, jobs in MBTI_JOBS.items():
        for item in jobs:
            if k in normalize(item["job"]):
                results.append({"type": t, "job": item["job"], "img": img_url(t, item["job"])})
    return results

# ------------------------------------------------------------
# 사이드바 안내
# ------------------------------------------------------------
with st.sidebar:
    st.header("🔎 사용 방법")
    st.markdown(
        "- 드롭다운에서 **MBTI**를 선택하면 해당 유형 추천 직업이 보여요.\n"
        "- 위 검색창에 **직업명** 일부를 입력하면 MBTI와 무관하게 전체에서 검색돼요.\n"
        "- 이미지는 *picsum.photos* 시드 기반 정적 URL을 사용해 안정적으로 표시됩니다."
    )
    st.markdown("---")
    st.caption("교육용 데모입니다. 실제 진로 결정은 흥미·역량·환경 등을 종합 고려하세요.")

# ------------------------------------------------------------
# 헤더 & 입력
# ------------------------------------------------------------
st.title("💼 MBTI 기반 진로 추천")
st.caption("MBTI 성향과 직업 간의 **일반적 경향**을 보여주는 교육용 예시입니다.")

col1, col2 = st.columns([1, 2])
with col1:
    selected_mbti = st.selectbox("MBTI 선택", list(MBTI_JOBS.keys()), index=0)
with col2:
    keyword = st.text_input("직업명 검색 (예: 데이터, 간호, 디자이너)", placeholder="검색어를 입력하거나 비워두세요")

# ------------------------------------------------------------
# 데이터 준비
# ------------------------------------------------------------
if keyword.strip():
    data = filter_jobs(keyword)
    header = f"🔍 검색 결과 ({len(data)}건)"
else:
    data = [{"type": selected_mbti, "job": d["job"], "img": img_url(selected_mbti, d["job"]) } for d in MBTI_JOBS[selected_mbti]]
    header = f"🧭 {selected_mbti} 유형 추천 직업"

st.subheader(header)

# ------------------------------------------------------------
# 결과 렌더링 (카드형 3열)
# ------------------------------------------------------------
if not data:
    st.info("검색 결과가 없습니다. 다른 키워드를 시도해 보세요.")
else:
    cols = st.columns(3)
    for i, item in enumerate(data):
        with cols[i % 3]:
            with st.container(border=True):
                st.markdown(f"**[{item['type']}] {item['job']}**")
                st.image(item["img"], use_column_width=True)
                with st.popover("ℹ️ 설명"):
                    st.write(
                        "이 직업은 해당 MBTI의 일반적인 강점과 비교적 잘 맞는다고 알려져 있습니다.\n"
                        "실제 적합성은 개인의 경험·역량·흥미에 따라 크게 달라집니다."
                    )

# ------------------------------------------------------------
# 푸터
# ------------------------------------------------------------
st.markdown("---")
st.caption("이미지는 picsum.photos에서 제공하는 랜덤 이미지이며, 시드 고정으로 항상 표시됩니다.")
