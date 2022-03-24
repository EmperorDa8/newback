#!/usr/bin/env python3
from PIL import Image
import os

path="/supplier-data/images/"
location=os.getcwd()+path

def extract_data():
    for item in os.listdir(location):
        if item.endswith(".tiff"):
            img=Image.open(location+item).convert("RGB")
            img.resize((600,400)).save(location+item.replace("tiff", "jpeg"))
            print("process done")

extract_data()
