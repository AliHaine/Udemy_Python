import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
	st.image("images/fizz.jpg")
	st.text("test")

with col2:
	st.title("The title")
	st.text("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

st.text("text aafter asdasdsadsa as fasffafg aefea etatrtrew tewtewt ewqtqt qt q")