import os
from pathlib import Path


PATH_TO_IMAGES = Path.cwd() / 'pkmn_images'


for i, img in enumerate(os.listdir(PATH_TO_IMAGES), start=7):
	src_img = os.path.join(PATH_TO_IMAGES, str(i))
	pkmn_img = os.path.join(PATH_TO_IMAGES, str(i) + '.png')
	os.rename(src_img, pkmn_img)
