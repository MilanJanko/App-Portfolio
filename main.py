import streamlit as st
st.set_page_config(layout="wide")
col1, col2 =  st.columns(2)


with col1:
    st.image("images/Akica.jpg")

with col2:
    st.title('Milan Jankovic')
    content = """
    Hello, I am Milan,
     a passionate tech enthusiast and Python developer, 
     highly focused on data-centric solutions and driven by a 
     strong commitment to excellence. Also a pug lover!"""
    st.write(content)