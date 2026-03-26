import streamlit as st
from helper import todoFunctions

todos = todoFunctions.get_todos()

st.title("todo-app")
st.subheader("This is a todo app")
st.write("List your todos here")

for todo in todos:
    st.checkbox(todo.strip('\n'))

st.text_input(label="", placeholder='Add new todo...')