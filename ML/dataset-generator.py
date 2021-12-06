import os
import shutil
from PIL import Image

for file in os.listdir("images/"):
    file_array = file.split("_")
    directory = "dataset/" + file_array[0] + "/"
    name = file_array[1]
    
    if not os.path.exists(directory):
        os.makedirs(directory)
        
    im = Image.open(r"images/" + file)
    width, height = im.size

    left = width / 5
    top = height / 6
    bottom = height / 5 * 3
    right = width / 8 * 7

    im_crop = im.crop((left, top, right, bottom))

    print(name, im_crop.size)
    im_crop.save(directory + name)