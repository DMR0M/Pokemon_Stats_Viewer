import os
from pathlib import Path


PATH_TO_IMAGES = Path.cwd() / 'pkmn_images'


def png_conversion(gen_folder) -> None:
	gen_images = PATH_TO_IMAGES / gen_folder
	try:
		for i, img in enumerate(gen_images.iterdir(), start=1):
			src_img = os.path.join(gen_images, str(i))
			pkmn_img = os.path.join(gen_images, str(i) + '.png')
			os.rename(src_img, pkmn_img)
	except FileNotFoundError:
		print('Done')


def main():
	png_conversion('gen9')


if __name__ == '__main__':
	main()
