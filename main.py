import sys
from PIL import Image
import os

loc1 = sys.argv[1]
loc2 = sys.argv[2]

if not os.path.exists(loc2):
    os.makedirs(loc2)

for filename in os.listdir(loc1):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img = Image.open(f'{loc1}{filename}')
        new_file = os.path.splitext(filename)[0]
        img.save(f'{loc2}{new_file}.png', 'png')
