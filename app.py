# Created project file using script
from pathlib import Path
import streamlit as st
import pandas as pd
# import plotly.express as px
from PIL import Image


CSV_PATH = Path.cwd() / 'csv'

# List of Pokemon Data Sets
pkmn_data_sets = CSV_PATH.iterdir()

# Web page configuration
st.set_page_config(
	page_title='Pokemon Stats Viewer',
	layout="wide"
)

st.image('static/pokeball.png', width=60)
st.markdown('***')

st.header('Pokemon Stats Viewer')

st.subheader('View pokemon stats for each generation')

gen_list_headers = [f'Generation {str(n)} Pokemons: ' for n in range(1, 10)]

# Load dataframes and display to app
for i, csv in enumerate(pkmn_data_sets):
	st.subheader(gen_list_headers[i])

	pkmn_dataframe = pd.read_csv(csv)
	st.dataframe(pkmn_dataframe)
