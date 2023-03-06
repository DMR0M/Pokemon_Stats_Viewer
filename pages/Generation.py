from pathlib import Path
import streamlit as st
import pandas as pd
import template


CSV_PATH = Path.cwd() / 'csv'

# Gen 1
Gen_1 = CSV_PATH / 'pkmn_dataset_gen1.csv'
Gen_2 = CSV_PATH / 'pkmn_dataset_gen2.csv'
Gen_3 = CSV_PATH / 'pkmn_dataset_gen3.csv'

# List of Pokémon Data Sets
pkmn_data_sets = CSV_PATH.iterdir()
gen_df1 = pd.read_csv(Gen_1)
gen_df2 = pd.read_csv(Gen_2)
gen_df3 = pd.read_csv(Gen_3)

# Description Column
desc_columns = list(gen_df1.keys()[:5])

# Stats Column
stat_columns = list(gen_df1.keys()[5:])

st.set_page_config(
	page_title='Pokemon Stats Viewer',
	page_icon='static/pokeball.png',
	layout="wide",
)

template.header()

st.header('Generation 1 Pokémon')
st.markdown('***')
col_1, col_2, col_3, col_4, col_5 = st.columns([2.5, 2.5, 2.5, 2.5, 2.5])

# Iterate each dataframe and their values by slicing
# to display on each column
with col_1:
	# Set CSS Style for titles
	pkdx_num_title = '<p style="font-family:sans-serif Verdana; color:Black; font-size: 20px;">Pokédex Number: </p>'
	type_title = '<p style="font-family:sans-serif Verdana; color:Black; font-size: 28px;">Type: </p>'
	ability_title = '<p style="font-family:sans-serif Verdana; color:Black; font-size: 28px;">Ability: </p>'

	for i, row in gen_df1[:30].iterrows():
		st.markdown(pkdx_num_title, unsafe_allow_html=True)
		st.subheader(f". {row['Pokedex_Number']}"[2:])
		st.header(row['Name'])
		st.image(f"pages/gen1/{i + 1}.png", width=100)

		st.markdown(type_title, unsafe_allow_html=True)
		st.text(row['Type'])

		st.markdown(ability_title, unsafe_allow_html=True)
		st.text(row['Ability'])
		st.markdown('***')

with col_2:
	for i, row in gen_df1[30:60].iterrows():
		st.markdown(pkdx_num_title, unsafe_allow_html=True)
		st.subheader(f". {row['Pokedex_Number']}"[2:])
		st.header(row['Name'])
		st.image(f"pages/gen1/{i + 1}.png", width=100)

		st.markdown(type_title, unsafe_allow_html=True)
		st.text(row['Type'])

		st.markdown(ability_title, unsafe_allow_html=True)
		st.text(row['Ability'])
		st.markdown('***')

with col_3:
	for i, row in gen_df1[60:90].iterrows():
		st.markdown(pkdx_num_title, unsafe_allow_html=True)
		st.subheader(f". {row['Pokedex_Number']}"[2:])
		st.header(row['Name'])
		st.image(f"pages/gen1/{i + 1}.png", width=100)

		st.markdown(type_title, unsafe_allow_html=True)
		st.text(row['Type'])

		st.markdown(ability_title, unsafe_allow_html=True)
		st.text(row['Ability'])
		st.markdown('***')

with col_4:
	for i, row in gen_df1[90:120].iterrows():
		st.markdown(pkdx_num_title, unsafe_allow_html=True)
		st.subheader(f". {row['Pokedex_Number']}"[2:])
		st.header(row['Name'])
		st.image(f"pages/gen1/{i + 1}.png", width=100)

		st.markdown(type_title, unsafe_allow_html=True)
		st.text(row['Type'])

		st.markdown(ability_title, unsafe_allow_html=True)
		st.text(row['Ability'])
		st.markdown('***')

with col_5:
	for i, row in gen_df1[120:].iterrows():
		st.markdown(pkdx_num_title, unsafe_allow_html=True)
		st.subheader(f". {row['Pokedex_Number']}"[2:])
		st.header(row['Name'])
		st.image(f"pages/gen1/{i + 1}.png", width=100)

		st.markdown(type_title, unsafe_allow_html=True)
		st.text(row['Type'])

		st.markdown(ability_title, unsafe_allow_html=True)
		st.text(row['Ability'])
		st.markdown('***')
