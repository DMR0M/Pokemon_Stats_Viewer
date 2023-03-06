import streamlit as st


def header():
    st.image('static/pokeball.png', width=60)
    st.markdown('***')

    st.header('Pokemon Stats Viewer')

    st.subheader('View pokemon stats for each generation')
