#! /usr/bin/env python3

import os
import requests

fpath = os.getcwd() + "/supplier-data/images/"
url = "http://localhost/fruits/post"

fruits = {}
for file in os.listdir(fpath):
    if file.endswith(".txt"):
        with open((fpath + file), "r") as f:
            WORDS = f.readlines()
    fruits["name"] = WORDS[0].strip("\n")
    fruits["weight"] = int(WORDS[1].strip("\n").strip("lbs"))
    fruits["description"] = WORDS[2].strip("\n")
    fruits["image_name"] = file.strip(".txt") + ".jpeg"
    r=requests.post(url, data=fruits)
