from PIL import Image
import os

loc1 = input('Name of the Folder where png images are stored: ')
loc2 = input('Name of the Output Folder: ')

loc1 = loc1 + '/'
loc2 = loc2 + '/'

if not os.path.exists(loc2):
    os.makedirs(loc2)

for filename in os.listdir(loc1):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img = Image.open(f'{loc1}{filename}')
        new_file = os.path.splitext(filename)[0]
        img.save(f'{loc2}{new_file}.png', 'png')
