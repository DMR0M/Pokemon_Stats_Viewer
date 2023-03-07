import streamlit as st


def display_pokemons(pkmn_df, header: str, gen_num: str):
	st.header(header)
	st.markdown('***')
	col_1, col_2, col_3, col_4, col_5 = st.columns([2.5, 2.5, 2.5, 2.5, 2.5])
	pkmn_df_length = len(pkmn_df) // 5
	pkmn_img_size = 125

	# Iterate each pkmn_df and their values by slicing
	# to display on each column
	with col_1:
		# Set CSS Style for titles
		pkdx_num_title = '<p style="font-family:sans-serif Verdana; color:Black; font-size: 18px;">Pokédex Number: </p>'
		type_title = '<p style="font-family:sans-serif Verdana; color:Black; font-size: 18px;">Type: </p>'
		ability_title = '<p style="font-family:sans-serif Verdana; color:Black; font-size: 18px;">Ability: </p>'

		for i, row in pkmn_df[:pkmn_df_length].iterrows():
			st.markdown(pkdx_num_title, unsafe_allow_html=True)
			st.subheader(f". {row['Pokedex_Number']}"[2:])
			st.header(row['Name'])
			img_num = row['Image'].split('.')[0]
			st.image(f"pages/gen{gen_num}/{img_num}.png", width=pkmn_img_size)

			st.markdown(type_title, unsafe_allow_html=True)
			st.text(row['Type'])

			st.markdown(ability_title, unsafe_allow_html=True)
			st.text(row['Ability'])
			st.markdown('***')

	with col_2:
		for i, row in pkmn_df[pkmn_df_length:pkmn_df_length*2].iterrows():
			st.markdown(pkdx_num_title, unsafe_allow_html=True)
			st.subheader(f". {row['Pokedex_Number']}"[2:])
			st.header(row['Name'])

			img_num = row['Image'].split('.')[0]
			st.image(f"pages/gen{gen_num}/{img_num}.png", width=pkmn_img_size)

			st.markdown(type_title, unsafe_allow_html=True)
			st.text(row['Type'])

			st.markdown(ability_title, unsafe_allow_html=True)
			st.text(row['Ability'])
			st.markdown('***')

	with col_3:
		for i, row in pkmn_df[pkmn_df_length*2:pkmn_df_length*3].iterrows():
			st.markdown(pkdx_num_title, unsafe_allow_html=True)
			st.subheader(f". {row['Pokedex_Number']}"[2:])
			st.header(row['Name'])

			img_num = row['Image'].split('.')[0]
			st.image(f"pages/gen{gen_num}/{img_num}.png", width=pkmn_img_size)

			st.markdown(type_title, unsafe_allow_html=True)
			st.text(row['Type'])

			st.markdown(ability_title, unsafe_allow_html=True)
			st.text(row['Ability'])
			st.markdown('***')

	with col_4:
		for i, row in pkmn_df[pkmn_df_length*3:pkmn_df_length*4].iterrows():
			st.markdown(pkdx_num_title, unsafe_allow_html=True)
			st.subheader(f". {row['Pokedex_Number']}"[2:])
			st.header(row['Name'])

			img_num = row['Image'].split('.')[0]
			st.image(f"pages/gen{gen_num}/{img_num}.png", width=pkmn_img_size)

			st.markdown(type_title, unsafe_allow_html=True)
			st.text(row['Type'])

			st.markdown(ability_title, unsafe_allow_html=True)
			st.text(row['Ability'])
			st.markdown('***')

	with col_5:
		for i, row in pkmn_df[pkmn_df_length*4:].iterrows():
			st.markdown(pkdx_num_title, unsafe_allow_html=True)
			st.subheader(f". {row['Pokedex_Number']}"[2:])
			st.header(row['Name'])

			img_num = row['Image'].split('.')[0]
			st.image(f"pages/gen{gen_num}/{img_num}.png", width=pkmn_img_size)

			st.markdown(type_title, unsafe_allow_html=True)
			st.text(row['Type'])

			st.markdown(ability_title, unsafe_allow_html=True)
			st.text(row['Ability'])
			st.markdown('***')

