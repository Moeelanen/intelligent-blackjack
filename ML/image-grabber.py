import os
import requests
import shutil

def grabImage(card):
    url = "http://192.168.197.139/capture"
    existing_same_count = len([name for name in os.listdir("images/") if (name.split("_")[0] == card)])
    filename = card + "_" + str(existing_same_count) + ".jpg"
    res = requests.get(url, stream=True)
    if res.status_code == 200:
        with open('images/'+filename, 'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print("Image successfully downloaded: ", filename)
    else:
        print("Image was not downloaded")


card_name = ""
while True:
    user_input = input("Name or enter: ")
    if (user_input != ""):
        card_name = user_input
    grabImage(card_name)

