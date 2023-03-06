from pathlib import Path
import streamlit as st
import pandas as pd
import template


CSV_PATH = Path.cwd() / 'csv'
print(CSV_PATH)
# Gen 1
Gen_1 = CSV_PATH / 'pkmn_dataset_gen1.csv'

# List of Pokémon Data Sets
pkmn_data_sets = CSV_PATH.iterdir()
gen_df1 = pd.read_csv(Gen_1)

st.set_page_config(
	page_title='Pokemon Stats Viewer',
	page_icon='static/pokeball.png',
	layout="wide",
)


st.header('Generation 1 Pokémon')
st.markdown('***')
col_1, col_2, col_3, col_4, col_5 = st.columns([2.5, 2.5, 2.5, 2.5, 2.5])


with col_1:
	for i, row in gen_df1[:30].iterrows():
		st.subheader('Pokedex Number: ')
		st.info(f"No. {row['Pokedex_Number']}"[2:])
		st.header(row['Name'])
		st.image(f"pages/gen1/{i + 1}.png", width=120)

		st.subheader('Type: ')
		st.subheader(row['Type'])

		st.subheader('Ability: ')
		st.info(row['Ability'])
		st.markdown('***')

with col_2:
	for i, row in gen_df1[30:60].iterrows():
		st.subheader('Pokedex Number: ')
		st.info(f"No. {row['Pokedex_Number']}"[2:])
		st.header(row['Name'])
		st.image(f"pages/gen1/{i + 1}.png", width=120)

		st.subheader('Type: ')
		st.subheader(row['Type'])

		st.subheader('Ability: ')
		st.info(row['Ability'])
		st.markdown('***')

with col_3:
	for i, row in gen_df1[60:90].iterrows():
		st.subheader('Pokedex Number: ')
		st.info(f"No. {row['Pokedex_Number']}"[2:])
		st.header(row['Name'])
		st.image(f"pages/gen1/{i + 1}.png", width=120)

		st.subheader('Type: ')
		st.subheader(row['Type'])

		st.subheader('Ability: ')
		st.info(row['Ability'])
		st.markdown('***')

with col_4:
	for i, row in gen_df1[90:120].iterrows():
		st.subheader('Pokedex Number: ')
		st.info(f"No. {row['Pokedex_Number']}"[2:])
		st.header(row['Name'])
		st.image(f"pages/gen1/{i + 1}.png", width=120)

		st.subheader('Type: ')
		st.subheader(row['Type'])

		st.subheader('Ability: ')
		st.info(row['Ability'])
		st.markdown('***')

with col_5:
	for i, row in gen_df1[120:].iterrows():
		st.subheader('Pokedex Number: ')
		st.info(f"No. {row['Pokedex_Number']}"[2:])
		st.header(row['Name'])
		st.image(f"pages/gen1/{i + 1}.png", width=120)

		st.subheader('Type: ')
		st.subheader(row['Type'])

		st.subheader('Ability: ')
		st.info(row['Ability'])
		st.markdown('***')
