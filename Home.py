# Created project file using script
from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px
from itertools import chain
import template
# from PIL import Image

CSV_PATH = Path.cwd() / 'csv'
pkmn_data_sets = CSV_PATH.iterdir()

# Web page configuration
st.set_page_config(
	page_title='Pokemon Stats Viewer',
	page_icon='static/pokeball.png',
	layout="wide",
)

template.header()

gen_list_headers = [f'Generation {str(n)} Pokemon: ' for n in range(1, 10)]

# Load dataframes and display to app
for i, csv in enumerate(pkmn_data_sets):
	st.subheader(gen_list_headers[i])

	pkmn_dataframe = pd.read_csv(csv)
	st.dataframe(pkmn_dataframe)

