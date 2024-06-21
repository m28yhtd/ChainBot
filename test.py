import streamlit as st
import time
import pyautogui

st.set_page_config(
    page_title = "test",
    page_icon = "👋"
)


def process():
    dial = pyautogui.confirm('오류를 발생시키겠습니까?', buttons=['Y', 'N'])

    if dial == 'Y':
        error_place = pyautogui.prompt('오류를 발생시킬 위치를 입력해주세요')
    else:
        error_place = None

    if error_place == None:
        st.write("this is not error!")
    else:
        st.write(error_place)


openai_api_key = "your_api_key(must be changed)"

st.title('test')

input = st.text_input("message")

process()
process()