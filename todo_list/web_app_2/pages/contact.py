import streamlit as st
from todo_list.web_app_2 import gmail_send

st.header("Contact")

with st.form(key="form"):
	email = st.text_input("Email")
	msg = st.text_area("Message")
	button = st.form_submit_button("Send")
	if button:
		gmail_send.gmail_send(email, msg)