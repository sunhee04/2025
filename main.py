# app.py
import streamlit as st
from typing import List, Dict

st.set_page_config(page_title="MBTI 기반 진로 추천", page_icon="💼", layout="wide")

# ------------------------------------------------------------
# 데이터: 16개 MBTI × 5개 직업 (표시명, 이미지 키워드)
# 이미지: Unsplash featured 검색(무료, 키워드 기반 랜덤 이미지)
# ------------------------------------------------------------
MBTI_JOBS: Dict[str, List[Dict[str, str]]] = {
    "ISTJ": [
        {"job": "회계사", "q": "accountant,finance,office"},
        {"job": "데이터 분석가", "q": "data analyst,analytics,charts"},
        {"job": "군인", "q": "soldier,army,uniform"},
        {"job": "품질관리 엔지니어", "q": "quality engineer,manufacturing"},
        {"job": "행정 공무원", "q": "civil servant,administration,documents"},
    ],
    "ISFJ": [
        {"job": "간호사", "q": "nurse,hospital,healthcare"},
        {"job": "초등교사", "q": "elementary teacher,classroom"},
        {"job": "사회복지사", "q": "social worker,community"},
        {"job": "비서", "q": "assistant,secretary,office"},
        {"job": "심리상담사", "q": "counselor,therapy,psychology"},
    ],
    "INFJ": [
        {"job": "심리학자", "q": "psychologist,therapy"},
        {"job": "작가", "q": "writer,books,notebook"},
        {"job": "교육 컨설턴트", "q": "education consultant,learning"},
        {"job": "사회운동가", "q": "activist,community,nonprofit"},
        {"job": "예술가", "q": "artist,studio,paint"},
    ],
    "INTJ": [
        {"job": "전략기획가", "q": "strategist,planning,whiteboard"},
        {"job": "데이터 사이언티스트", "q": "data scientist,ml,code"},
        {"job": "연구원", "q": "researcher,laboratory,science"},
        {"job": "경영 컨설턴트", "q": "management consultant,boardroom"},
        {"job": "시스템 엔지니어", "q": "systems engineer,network,architecture"},
    ],
    "ISTP": [
        {"job": "정비사", "q": "mechanic,workshop,tools"},
        {"job": "파일럿", "q": "pilot,airplane,cockpit"},
        {"job": "소방관", "q": "firefighter,fire station"},
        {"job": "경찰관", "q": "police officer,patrol"},
        {"job": "응급구조사", "q": "paramedic,ambulance,emergency"},
    ],
    "ISFP": [
        {"job": "패션 디자이너", "q": "fashion designer,studio"},
        {"job": "사진작가", "q": "photographer,camera,studio"},
        {"job": "요리사", "q": "chef,kitchen,restaurant"},
        {"job": "음악가", "q": "musician,studio,instrument"},
        {"job": "실내디자이너", "q": "interior designer,home,decor"},
    ],
    "INFP": [
        {"job": "작가", "q": "writer,poet,journal"},
        {"job": "상담가", "q": "counselor,therapy"},
        {"job": "번역가", "q": "translator,language,books"},
        {"job": "비영리단체 활동가", "q": "nonprofit worker,community"},
        {"job": "콘텐츠 기획자", "q": "content planner,creative,notion"},
    ],
    "INTP": [
        {"job": "연구원", "q": "researcher,laboratory"},
        {"job": "프로그래머", "q": "programmer,code,laptop"},
        {"job": "과학자", "q": "scientist,lab"},
        {"job": "발명가", "q": "inventor,prototype,workbench"},
        {"job": "데이터 분석가", "q": "data analyst,charts,python"},
    ],
    "ESTP": [
        {"job": "영업 전문가", "q": "salesperson,sales meeting"},
        {"job": "기업가", "q": "entrepreneur,startup,founder"},
        {"job": "스포츠 코치", "q": "sports coach,training"},
        {"job": "마케팅 전문가", "q": "marketer,marketing,campaign"},
        {"job": "이벤트 기획자", "q": "event planner,stage,event"},
    ],
    "ESFP": [
        {"job": "배우", "q": "actor,theater,stage"},
        {"job": "가수", "q": "singer,concert,microphone"},
        {"job": "여행 가이드", "q": "tour guide,travel"},
        {"job": "MC", "q": "host,emcee,event microphone"},
        {"job": "영업 매니저", "q": "sales manager,meeting"},
    ],
    "ENFP": [
        {"job": "광고 기획자", "q": "advertising planner,creative"},
        {"job": "홍보 전문가", "q": "public relations,press"},
        {"job": "작가", "q": "writer,creative,notes"},
        {"job": "심리 상담가", "q": "counselor,therapy"},
        {"job": "이벤트 플래너", "q": "event planner,planning"},
    ],
    "ENTP": [
        {"job": "기업가", "q": "entrepreneur,startup"},
        {"job": "마케팅 디렉터", "q": "marketing director,whiteboard"},
        {"job": "변호사", "q": "lawyer,courtroom"},
        {"job": "벤처 투자자", "q": "venture capitalist,vc,pitch"},
        {"job": "기술 혁신가", "q": "technology innovator,robotics"},
    ],
    "ESTJ": [
        {"job": "프로젝트 매니저", "q": "project manager,kanban"},
        {"job": "경영자", "q": "executive,ceo,boardroom"},
        {"job": "군 간부", "q": "military officer,uniform"},
        {"job": "행정관리자", "q": "administrative manager,office"},
        {"job": "영업 관리자", "q": "sales manager,crm"},
    ],
    "ESFJ": [
        {"job": "간호사", "q": "nurse,clinic"},
        {"job": "교사", "q": "teacher,classroom"},
        {"job": "HR 매니저", "q": "hr manager,human resources"},
        {"job": "상담사", "q": "counselor,meeting"},
        {"job": "영양사", "q": "dietitian,nutrition,kitchen"},
    ],
    "ENFJ": [
        {"job": "교육자", "q": "educator,teacher,leadership"},
        {"job": "리더십 코치", "q": "leadership coach,workshop"},
        {"job": "사회운동가", "q": "activist,community"},
        {"job": "심리상담사", "q": "therapist,counselor"},
        {"job": "홍보 전문가", "q": "public relations,media"},
    ],
    "ENTJ": [
        {"job": "경영 컨설턴트", "q": "management consultant,analytics"},
        {"job": "CEO", "q": "ceo,business leader,board"},
        {"job": "변호사", "q": "lawyer,contract"},
        {"job": "프로젝트 디렉터", "q": "project director,leadership"},
        {"job": "마케팅 전략가", "q": "marketing strategist,planning"},
    ],
}

# ------------------------------------------------------------
# 유틸
# ------------------------------------------------------------
def img_url_from_query(q: str, w: int = 1200) -> str:
    # Unsplash featured 이미지 (키워드 기반, 랜덤)
    # 상업 서비스 전 배포 시에는 라이선스/출처 정책을 반드시 확인하세요.
    return f"https://source.unsplash.com/featured/?{q.replace(' ', '%20')}"

def normalize(s: str) -> str:
    return "".join(s.lower().split())

def filter_jobs(keyword: str) -> List[Dict]:
    """검색 키워드로 MBTI 전체에서 직업 필터링"""
    k = normalize(keyword)
    results = []
    for t, jobs in MBTI_JOBS.items():
        for item in jobs:
            if k in normalize(item["job"]):
                results.append({"type": t, "job": item["job"], "q": item["q"]})
    return results

# ------------------------------------------------------------
# 사이드바: 사용 도움말
# ------------------------------------------------------------
with st.sidebar:
    st.header("🔎 사용 방법")
    st.markdown(
        "- 드롭다운에서 **MBTI**를 선택하면 해당 유형 추천 직업이 나와요.\n"
        "- 상단 검색창에 **직업명**(예: 데이터, 간호) 일부만 입력해도 검색돼요.\n"
        "- ⭐ 버튼으로 직업을 **즐겨찾기**해두면 나중에 다시 볼 수 있어요."
    )
    st.markdown("---")
    st.caption("이미지는 Unsplash featured를 사용한 예시입니다. 실제 서비스 배포 시 라이선스/출처 정책을 확인하세요.")

# 세션 상태(즐겨찾기)
if "favorites" not in st.session_state:
    st.session_state.favorites = []  # 각 항목: dict(type, job, q)

# ------------------------------------------------------------
# 헤더
# ------------------------------------------------------------
st.title("💼 MBTI 기반 진로 추천")
st.caption("교육용 예시 — MBTI 성향과 직업 간 연관은 일반화된 경향성일 뿐, 절대적인 지침이 아닙니다.")

# ------------------------------------------------------------
# 입력 영역
# ------------------------------------------------------------
col_mbti, col_search = st.columns([1, 2])
with col_mbti:
    selected_mbti = st.selectbox("MBTI 선택", list(MBTI_JOBS.keys()), index=0)
with col_search:
    keyword = st.text_input("직업명 검색 (예: 데이터, 간호, 디자이너 등)", placeholder="검색어를 입력하거나 비워두세요")

# ------------------------------------------------------------
# 데이터 준비
# ------------------------------------------------------------
if keyword.strip():
    # 검색 모드: 전체 MBTI에서 필터링
    data = filter_jobs(keyword)
    header = f"🔍 검색 결과 ({len(data)}건)"
else:
    # MBTI 모드: 해당 MBTI의 직업 리스트
    data = [{"type": selected_mbti, "job": d["job"], "q": d["q"]} for d in MBTI_JOBS[selected_mbti]]
    header = f"🧭 {selected_mbti} 유형 추천 직업"

st.subheader(header)

# ------------------------------------------------------------
# 결과 렌더링 (카드형, 3열 그리드)
# ------------------------------------------------------------
if not data:
    st.info("검색 결과가 없습니다. 다른 키워드를 시도해 보세요.")
else:
    # 3열 그리드
    cols = st.columns(3)
    for i, item in enumerate(data):
        with cols[i % 3]:
            with st.container(border=True):
                st.markdown(f"**[{item['type']}] {item['job']}**")
                st.image(img_url_from_query(item["q"]), use_column_width=True)
                c1, c2 = st.columns([1, 1])
                with c1:
                    # 즐겨찾기 토글
                    is_fav = any((f["type"] == item["type"] and f["job"] == item["job"]) for f in st.session_state.favorites)
                    label = "⭐ 즐겨찾기" if not is_fav else "✅ 저장됨"
                    if st.button(label, key=f"fav-{item['type']}-{item['job']}"):
                        if not is_fav:
                            st.session_state.favorites.append(item)
                        else:
                            st.session_state.favorites = [
                                f for f in st.session_state.favorites
                                if not (f["type"] == item["type"] and f["job"] == item["job"])
                            ]
                        st.experimental_rerun()
                with c2:
                    # 간단 설명(예시)
                    with st.popover("ℹ️ 간단 설명"):
                        st.write(
                            "이 직업은 MBTI의 일반적인 강점(성향, 문제해결 방식, 대인관계 스타일 등)과 "
                            "업무 특성이 비교적 잘 맞는다고 알려져 있습니다. 실제 적합성은 "
                            "경험, 역량, 관심사에 따라 크게 달라질 수 있습니다."
                        )

# ------------------------------------------------------------
# 즐겨찾기 영역
# ------------------------------------------------------------
st.markdown("---")
st.subheader(f"⭐ 즐겨찾기 ({len(st.session_state.favorites)}건)")
if not st.session_state.favorites:
    st.write("아직 즐겨찾기한 직업이 없습니다.")
else:
    fav_cols = st.columns(4)
    for i, fav in enumerate(st.session_state.favorites):
        with fav_cols[i % 4]:
            with st.container(border=True):
                st.markdown(f"**[{fav['type']}] {fav['job']}**")
                st.image(img_url_from_query(fav["q"]), use_column_width=True)
                if st.button("🗑️ 삭제", key=f"del-{fav['type']}-{fav['job']}"):
                    st.session_state.favorites = [
                        f for f in st.session_state.favorites
                        if not (f["type"] == fav["type"] and f["job"] == fav["job"])
                    ]
                    st.experimental_rerun()
