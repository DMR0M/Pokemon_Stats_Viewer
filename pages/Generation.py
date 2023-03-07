from pathlib import Path
import streamlit as st
import pandas as pd
import template
import pokemons
from typing import NamedTuple

################################################################################
# Data
################################################################################
CSV_PATH = Path.cwd() / 'csv'


# Iteration through the path to csv files
def generate_csv_path(path):
	for csv_file in path.iterdir():
		yield csv_file


# List of Pokémon Data Sets
# Generator to iterate through list of data frames
generation_data_frames = (
	pd.read_csv(file)
	for file in generate_csv_path(CSV_PATH)
)

# List of Headers
gen_list_headers = [f'Generation {str(n)} ' for n in range(1, 10)]

# Dictionary of Generation and Pokemon Data
pokemon_data: dict = {
		key: val
		for key, val in zip
		(
			gen_list_headers,
			generation_data_frames,
		)
}

################################################################################
# Web Page
################################################################################

st.set_page_config(
	page_title='Pokemon Stats Viewer',
	page_icon='static/pokeball.png',
	layout="wide",
)

# Display page header
template.header()

# Add filtering selection for the selected
# generations of Pokemon
gen_options = st.selectbox(
	'Generation',
	list(pokemon_data.keys()),
)

pokemons.display_pokemons(
	pokemon_data[gen_options],
	gen_options,
	gen_options.split()[1],
)

