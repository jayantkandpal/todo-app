import streamlit as st
from helper import todoFunctions

todos = todoFunctions.get_todos()

def add_todo():
    new_todo = st.session_state["new_todo"] + '\n'
    todos.append(new_todo)
    todoFunctions.write_todos(todos)

st.title("todo-app")
st.subheader("This is a todo app")
st.write("List your todos here")

for todo in todos:
    st.checkbox(todo.strip('\n'))

st.text_input(label="Todo", placeholder='Add new todo...',
              on_change=add_todo, key='new_todo')

st.session_state