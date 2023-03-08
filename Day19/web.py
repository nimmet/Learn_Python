import streamlit as st
import functions

todos = functions.get_todos()
st.title("My Todo App")
st.subheader("This is sub header")
st.write("Todo app")


st.checkbox("Learn Python")
st.checkbox("Prepare for Pentest Certification")

for td in todos:
    st.checkbox(td)
    
st.text_input(label="",placeholder="Add new todo...")