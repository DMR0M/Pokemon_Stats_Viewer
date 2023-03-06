import streamlit as st


def header():
    col1, col2 = st.columns([0.5, 3])

    with col1:
        st.image('static/pokeball.png', width=120)

    with col2:
        st.header('Pokemon Stats Viewer')
        st.subheader('View pokemon stats for each generation')

    st.markdown('***')
