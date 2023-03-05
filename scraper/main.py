# Created package files using script
from pathlib import Path
from typing import Generator
from bs4 import BeautifulSoup
import requests
import urllib.request
import re
import json
import logging
import pandas as pd


# Serebii.net
url_1 = 'https://www.serebii.net/scarletviolet/pokemon.shtml'

# TODO: SCRAPE IMAGE OF POKEMON IN THIS URL
url_2 = 'https://www.serebii.net/pokemon/gen9pokemon.shtml'

RESPONSE = requests.get(url_2)

page = urllib.request.urlopen(url_2)
soup = BeautifulSoup(page, 'html.parser')
IMAGES_PATH = Path.cwd() / 'pkmn_images'

PKMN_TABLE = soup.find('table', class_='tab')
PKMN_DATA = soup.find_all('td', class_='fooinfo')

IMG_DATA = soup.find_all('img', class_='listsprite')
PKMN_TYPES = soup.find_all('td', class_='fooinfo')[3::11]


# Get the types
type_pattern = re.compile(r'(\w+)\.gif')
pkmn_types = []
for line in PKMN_TYPES:
	pkmn_types.append(re.findall(type_pattern, str(line)))


# Get images of pokemons
def get_img_serebii_page():
	for i, img in enumerate(IMG_DATA):
		img_src = img['src']
		urllib.request.urlretrieve(f'https://serebii.net{img_src}', str(i))
		print(f'Done downloading image from {img_src}')


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
pkmn_data: list[dict] = [
	{
			'Pokedex_Number': pkdx_n,
			'Name': nm,
			'Sprite': img,
			'Types': ', '.join(map(lambda x: x.title(), typ)),
			'Ability': abty,
			'Hp': hp,
			'Attack': atk,
			'Defense': de,
			'Sp. Attack': spatk,
			'Sp. Defense': spdef,
			'Speed': spd,
	} for pkdx_n, nm, img, typ, abty, hp, atk, de, spatk, spdef, spd
	in zip(pkdx_num, pkmn_name, pokemon_img, pkmn_types, pkmn_ability,
		hp_cols, atk_cols, def_cols, spatk_cols, spdef_cols, speed_cols,)
]

# Logger
print(json.dumps(pkmn_data, indent=2))

pkmn_dataframe = pd.DataFrame(pkmn_data)
pkmn_dataframe.to_csv(Path.cwd().parent / 'csv' / 'pkmn_data_gen9.csv', index=False, header=True)
