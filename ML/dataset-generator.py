import os
import shutil
from PIL import Image

for file in os.listdir("images/"):
    file_array = file.split("_")
    test_directory = "dataset/test/" + file_array[0] + "/"
    train_directory = "dataset/train/" + file_array[0] + "/"
    name = file_array[1]
    
    if not os.path.exists(test_directory):
        os.makedirs(test_directory)
    
    if not os.path.exists(train_directory):
        os.makedirs(train_directory)
        
    im = Image.open(r"images/" + file)
    width, height = im.size

    left = width / 5
    top = height / 6
    bottom = height / 5 * 3
    right = width / 8 * 7

    im_crop = im.crop((left, top, right, bottom))

    print(name, im_crop.size)
    if (int(name.split(".")[0]) > 25):
        im_crop.save(test_directory + name)
    else:
        im_crop.save(train_directory + name)