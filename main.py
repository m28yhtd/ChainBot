import streamlit as st

st.set_page_config(
    page_title = "main",
    page_icon = "👋"
)

openai_api_key = "your_api_key(must be changed)"

st.title('test')

input = st.text_input("message")
st.write(input)

st.session_state['user_input'] = input
