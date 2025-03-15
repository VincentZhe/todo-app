import streamlit as st
from decorator import append

import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo APP")
st.subheader("This is my to do APP.")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a new todo here...", on_change=add_todo,
              key="new_todo")


