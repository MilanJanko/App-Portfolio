import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(page_title='Portfolio', layout="wide")


# Defining a function to resize image for web app, in order to make UI better.#
def resize_image(imag):
    image_path = "images/" + imag
    image_size = (500, 350)
    resized = Image.open(image_path)
    resized = resized.resize(image_size, Image.ANTIALIAS)
    return resized


col1, col2 = st.columns(2)

with col1:
    st.image("images/Akica.jpg")

with col2:
    st.title('Milan Jankovic')
    content = """
    Hello, I am Milan,
     a passionate tech enthusiast and Python developer, 
     highly focused on data-centric solutions and driven by a 
     strong commitment to excellence. I finished my Master's Degree in 2017 in Nis, 
     at Faculty of Electronics, with main field of research concentrated in signal analysis.
     That brought me to learn Python and find ways to process,
     analyse and display data for my clients, so they have data-driven decisions, based on
     in-depth market or company research. In my spare time, I like running and playing God of War, especially 
     new one. Also a pug lover!"""
    st.write(content)

st.markdown("""
<style>
.big-font {
    font-size:20px !important;
    color: #1F1F1F;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)
st.markdown("<p class='big-font'> Below you can find more information about my "
            "projects and what I enjoy doing and spending time at."
            " By the way, picture above shows my small mops called Aki."
            " He enjoys walking all the time!</p>", unsafe_allow_html=True)

col3, empty_col, col4 = st.columns([3, 1, 3])
df = pd.read_csv("projects.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        img = resize_image(row['image'])
        st.image(img)
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        img = resize_image(row['image'])
        st.image(img)
        st.write(f"[Source code]({row['url']})")
