# Created project file using script
from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px
from itertools import chain
import template
# from PIL import Image


CSV_PATH = Path.cwd() / 'csv'
# Gen 1
Gen_1 = CSV_PATH / 'pkmn_dataset_gen1.csv'
Gen_2 = CSV_PATH / 'pkmn_dataset_gen2.csv'
Gen_3 = CSV_PATH / 'pkmn_dataset_gen3.csv'

# List of Pokemon Data Sets
pkmn_data_sets = CSV_PATH.iterdir()
gen_df1 = pd.read_csv(Gen_1)
gen_df2 = pd.read_csv(Gen_2)
gen_df3 = pd.read_csv(Gen_3)

# Description Column
desc_columns = list(gen_df1.keys()[:5])

# Stats Column
stat_columns = list(gen_df1.keys()[5:])


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

