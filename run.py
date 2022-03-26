#!/usr/bin/env python3

import os
import requests
import json


path="/supplier_data/descriptions/"
full_path=os.getcwd()+path

def upload_desc():
  for item in os.listdir(full_path):
    if item.endswith(".txt"):
      fruit_name=os.path.splitext(item)[0]
      with open(full_path+item,"r") as f:
        data=f.read().split("\n")
        fruit_data= {"name":data[0], "weight":data[1].strip(" lbs"), "description":data[2], "image_name":fruit_name+(".jpeg")
        r = requests.post(url, json=fruit_data)
        print (r.status_code)
        print ("upload success")

upload_desc()

