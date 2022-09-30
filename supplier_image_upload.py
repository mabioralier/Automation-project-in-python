#!/usr/bin/env python3

import requests
import os

url = "http://localhost/upload/post"

fpath = os.getcwd() + "/supplier-data/images/"
for image in os.listdir(fpath):
    if image.endswith(".jpeg"):
        newPath = fpath + image 
        with open(newPath, "rb") as opened:
            r=requests.post(url,files={"file":opened})
