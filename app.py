# Created project file using script
from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px
import template
# from PIL import Image


CSV_PATH = Path.cwd() / 'csv'
# Gen 1
Gen_1 = CSV_PATH / 'pkmn_dataset_gen1.csv'
Gen_2 = CSV_PATH / 'pkmn_dataset_gen2.csv'

# List of Pokemon Data Sets
pkmn_data_sets = CSV_PATH.iterdir()
gen_df1 = pd.read_csv(Gen_1)
gen_df2 = pd.read_csv(Gen_2)

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

st.header('Generation 1 Pokemon')
st.markdown('***')
col_1, col_2, col_3, col_4 = st.columns([1, 1, 1, 1])

with col_1:
	for i, row in gen_df1[:38].iterrows():
		st.info(row['Pokedex_Number'][2:])
		st.header(row['Name'])
		st.image(f"gen1/{i + 1}.png", width=160)
		st.subheader(row['Type'])
		st.info(row['Ability'])
		st.markdown('***')

with col_2:
	for i, row in gen_df1[38:76].iterrows():
		st.info(row['Pokedex_Number'][2:])
		st.header(row['Name'])
		st.image(f"gen1/{i + 1}.png", width=160)
		st.subheader(row['Type'])
		st.info(row['Ability'])
		st.markdown('***')

with col_3:
	for i, row in gen_df1[76:114].iterrows():
		st.info(row['Pokedex_Number'][2:])
		st.header(row['Name'])
		st.image(f"gen1/{i + 1}.png", width=160)
		st.subheader(row['Type'])
		st.info(row['Ability'])
		st.markdown('***')

with col_4:
	for i, row in gen_df1[114:].iterrows():
		st.info(row['Pokedex_Number'][2:])
		st.header(row['Name'])
		st.image(f"gen1/{i + 1}.png", width=160)
		st.subheader(row['Type'])
		st.info(row['Ability'])
		st.markdown('***')


st.header('Generation 2 Pokemon')
st.markdown('***')
col_5, col_6, col_7, col_8 = st.columns([1, 1, 1, 1])

with col_5:
	for i, row in gen_df2[:25].iterrows():
		st.info(row['Pokedex_Number'][2:])
		st.header(row['Name'])
		st.image(f"gen2/{i + 1}.png", width=160)
		st.subheader(row['Type'])
		st.info(row['Ability'])
		st.markdown('***')

with col_6:
	for i, row in gen_df2[25:50].iterrows():
		st.info(row['Pokedex_Number'][2:])
		st.header(row['Name'])
		st.image(f"gen2/{i + 1}.png", width=160)
		st.subheader(row['Type'])
		st.info(row['Ability'])
		st.markdown('***')

with col_7:
	for i, row in gen_df2[50:75].iterrows():
		st.info(row['Pokedex_Number'][2:])
		st.header(row['Name'])
		st.image(f"gen2/{i + 1}.png", width=160)
		st.subheader(row['Type'])
		st.info(row['Ability'])
		st.markdown('***')

with col_8:
	for i, row in gen_df2[100:].iterrows():
		st.info(row['Pokedex_Number'][2:])
		st.header(row['Name'])
		st.image(f"gen2/{i + 1}.png", width=160)
		st.subheader(row['Type'])
		st.info(row['Ability'])
		st.markdown('***')
