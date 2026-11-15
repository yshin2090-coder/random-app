import random
import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="점심 메뉴 추천기", page_icon="🍱")

# 제목 및 안내 문구
st.title("🍱 오늘의 점심 메뉴 추천기")
st.write("버튼을 누르면 오늘 먹을 점심 메뉴를 랜덤으로 추천해 줍니다!")

# 추천할 점심 메뉴 리스트
menus = [
    "김치찌개",
    "된장찌개",
    "제육볶음",
    "돈가스",
    "비빔밥",
    "짜장면",
    "짬뽕",
    "초밥",
    "햄버거",
    "파스타",
    "순대국밥",
    "쌀국수",
    "떡볶이",
    "마라탕",
    "샌드위치",
]

# 버튼을 눌렀을 때 실행될 동작
if st.button("메뉴 추천받기 🎲", use_container_width=True):
  choice = random.choice(menus)
  st.success(f"오늘의 추천 메뉴는 **{choice}**입니다!")
  st.balloons()
