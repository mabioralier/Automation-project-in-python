#!/usr/bin/env python3
from PIL import Image
import os
fpath = os.getcwd() + "/supplier-data/images/"
size = (600,400)

for file in os.listdir(fpath):
    if file.endswith(".tiff"):
        file_path,_=os.path.splitext(fpath + file)
        im = Image.open(fpath + file)
        new_path = "{}.jpeg".format(file_path)
        im.convert("RGB").resize(size).save(new_path,"JPEG")
        
