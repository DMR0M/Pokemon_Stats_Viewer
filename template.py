import streamlit as st


def header():
    col1, col2 = st.columns([0.5, 3])
    # Set CSS Style for Subtitle
    subtitle = '<p style="font-family:sans-serif Verdana; color:Black; font-size: 30px;">Pokédex Number: </p>'

    with col1:
        st.image('static/pokeball.png', width=120)

    with col2:
        st.header('Pokémon Stats Viewer')
        st.markdown('View pokemon stats for each generation', unsafe_allow_html=True)

    st.markdown('***')
