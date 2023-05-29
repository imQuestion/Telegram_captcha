import random
import os


list_callback = [
    "Ali sorena",
    "aliG",
    "banana",
    "Batman",
    "Hiphopologist",
    "ho3ein",
    "khalse",
    "mango",
    "medgal",
    "Michael",
    "moon",
    "mr_robot",
    "orange",
    "pishro",
    "Putak",
    "Sadegh",
    "Shayea",
    "sun",
    "T_bag",
    "Yas"
]

def captcha(path):
    random_items = random.sample(list_callback, 3)
    image_folder = path
    image_files = os.listdir(image_folder)
    random_image = random.choice(image_files)
    while any(word in random_image for word in random_items):
        random_image = random.choice(image_files)
    no_jpg = random_image.split(".")
    random_items.append(no_jpg[0])
    return random_items, random_image

