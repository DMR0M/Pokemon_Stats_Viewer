# Created package files using script
from pathlib import Path
from typing import Generator
from bs4 import BeautifulSoup
import requests
import urllib.request
import re
import json
# import logging
import pandas as pd


# Serebii.net
url = 'https://www.serebii.net/scarletviolet/pokemon.shtml'


url_1 = 'https://www.serebii.net/pokemon/gen1pokemon.shtml'
url_2 = 'https://www.serebii.net/pokemon/gen2pokemon.shtml'
url_3 = 'https://www.serebii.net/pokemon/gen3pokemon.shtml'
url_4 = 'https://www.serebii.net/pokemon/gen4pokemon.shtml'
url_5 = 'https://www.serebii.net/pokemon/gen5pokemon.shtml'
url_6 = 'https://www.serebii.net/pokemon/gen6pokemon.shtml'
url_7 = 'https://www.serebii.net/pokemon/gen7pokemon.shtml'
url_8 = 'https://www.serebii.net/pokemon/gen8pokemon.shtml'
url_9 = 'https://www.serebii.net/pokemon/gen9pokemon.shtml'

RESPONSE = requests.get(url_8)

page = urllib.request.urlopen(url_8)
soup = BeautifulSoup(page, 'html.parser')
IMAGES_PATH = Path.cwd() / 'pkmn_images'

PKMN_DATA = soup.find_all('td', class_='fooinfo')
IMG_DATA = soup.find_all('td', class_='fooinfo')[1::11]
PKMN_TYPES = soup.find_all('td', class_='fooinfo')[3::11]

# print(PKMN_DATA)
# print(IMG_DATA)

# Get the types
type_pattern = re.compile(r'(\w+)\.gif')
pkmn_types = []
for line in PKMN_TYPES:
	pkmn_types.append(re.findall(type_pattern, str(line)))


# Get images of pokemons
img_pattern = re.compile(r'src="([^"]+)')
image_endpoint = re.findall(img_pattern, ''.join(map(str, IMG_DATA)))


# Function to scrape the pokemon sprite images in Serebii.net
def get_img_serebii_page(gen_folder) -> None:
	for i, img in enumerate(image_endpoint, start=1):
		urllib.request.urlretrieve(f'https://serebii.net{img}', IMAGES_PATH / gen_folder / str(i))
		print(f'Done downloading image from https://serebii.net{img}')


# Generate pokemon data from selector
def pkmn_data(html) -> Generator:
	for pkmn in html:
		if pkmn:
			yield pkmn.text.strip()


pokemon_list = list(filter(lambda x: x, [pokemon for pokemon in pkmn_data(PKMN_DATA)]))
pokemon_img = list(map(lambda x: Path(x).name, IMAGES_PATH.iterdir()))
pokemon_img.sort(key=lambda f: int(re.sub(r'\D', '', f)))

# print(*pokemon_list, sep='\n')
# List Distibutions
pkdx_num = pokemon_list[::9]
pkmn_name = pokemon_list[1::9]
pkmn_ability = pokemon_list[2::9]
hp_cols = pokemon_list[3::9]
atk_cols = pokemon_list[4::9]
def_cols = pokemon_list[5::9]
spatk_cols = pokemon_list[6::9]
spdef_cols = pokemon_list[7::9]
speed_cols = pokemon_list[8::9]

# Create dictionary
pkmn_dict: list[dict] = [
	{
			'Pokedex_Number': pkdx_n,
			'Name': nm,
			'Type': ', '.join(map(lambda x: x.title(), typ)),
			'Ability': abty,
			'Hp': hp,
			'Attack': atk,
			'Defense': de,
			'Sp. Attack': spatk,
			'Sp. Defense': spdef,
			'Speed': spd,
	} for pkdx_n, nm, typ, abty, hp, atk, de, spatk, spdef, spd
	in zip(pkdx_num, pkmn_name, pkmn_types, pkmn_ability,
		hp_cols, atk_cols, def_cols, spatk_cols, spdef_cols, speed_cols,)
]

# Logger
# print(json.dumps(pkmn_data, indent=2))


def convert_to_csv(csv_filename, data) -> None:
	pkmn_dataframe = pd.DataFrame(data)
	if csv_filename.endswith('.csv'):
		pkmn_dataframe.to_csv(Path.cwd().parent / 'csv' / csv_filename, index=False, header=True)
	else:
		print('Not a valid filename')


def convert_to_json(file) -> None:
	with open(Path.cwd().parent / 'json' / file, 'w', encoding='utf-8') as f:
		json_data = json.dumps(pkmn_data, indent=2)
		f.write(json_data)


def main():
	while True:
		try:
			user_input = int(input('Type what generation [1-9]: '))
			if (user_input < 10) and (user_input > 0):
				convert_to_csv(f'pkmn_dataset_gen{user_input}.csv', pkmn_dict)
				get_img_serebii_page(f'gen{user_input}')
				break
			else:
				print('Invalid Generation')
		except ValueError:
			print('Input was not a number')


if __name__ == '__main__':
	main()

