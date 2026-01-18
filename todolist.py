import streamlit as st
import pandas as pd

st.title("Todo list")
st.header("➕ Add Task")

# initialize empty list
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# input box
task = st.text_input("Enter a task")

# add button
if st.button("Add Task"):
    if task != "":
        st.session_state.tasks.append(task)
        st.success("Task added")
        st.rerun()
        
    else:
        st.warning("Please enter a task")
    
# display tasks
st.header("read")
if len(st.session_state.tasks)  ==0:
    st.info("No task added yet")
else:
    for t in (st.session_state.tasks):
        st.write(f"{t}")

#update
st.header(" Update Task")
if st.session_state.tasks:
    index = st.selectbox("Select task index", range(len(st.session_state.tasks)))
    new_task = st.text_input("Update task", st.session_state.tasks[index])

    if st.button("Update Task"):
        st.session_state.tasks[index] = new_task
        st.success("Task updated")
        st.rerun()  
    if len(st.session_state.tasks)  ==0:
        st.info("No task added yet")
    else:
        for t in (st.session_state.tasks):
            st.write(f"{t}")   

#Delete
st.header("Delete Task")
if st.session_state.tasks:
    del_index = st.selectbox("Select task index to delete", range(len(st.session_state.tasks)))

    if st.button("Delete Task"):
        st.session_state.tasks.pop(del_index)
        st.success("Task deleted")
        st.rerun()                   


