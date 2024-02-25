import streamlit as st
import function


def add_todo():
	function.write_to_todos_list(st.session_state["text_input1"])
	function.write_to_file()
	st.session_state["text_input1"] = ""


st.title("todo online")

for key, value in st.session_state.items():
	if not key.isnumeric():
		continue
	if value:
		function.remove_from_todos_list(int(key))
		function.write_to_file()
for todo in function.get_todos_list():
	st.checkbox(todo, key=function.get_index_of(todo))
st.text_input(label="", on_change=add_todo, placeholder="Add new todo", key="text_input1")
