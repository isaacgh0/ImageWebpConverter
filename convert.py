from PIL import Image
import os

print('This script converts images to webp format, put images in the same directory\nas this script, the images will be saved in the output directory as webp format')

img_format = input('Enter the format of the image: ')
quality = int(input('Enter the quality of the image (1 - 100): '))

script_dir = os.path.dirname(os.path.abspath(__file__))
files = os.listdir(script_dir)

images = [file for file in files if file.endswith(f'.{img_format}')]

output_dir = os.path.join(script_dir, 'output')
os.makedirs(output_dir, exist_ok = True)

for index, img in enumerate(images):
  refactored = f'{img}.webp'.replace(f'.{img_format}', '')
  final_path = os.path.join(output_dir, refactored)

  image = Image.open(os.path.join(script_dir, img))
  image = image.convert('RGB')
  image.save(final_path, 'webp', optimize = True, quality = quality)

  print(f'Done {index}', end = '\r')

print('Done converting images to webp format')