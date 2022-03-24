#!/usr/bin/env python3
from multiprocessing import Pool
import requests
import os



def image_upload(x):
    if x.endswith("jpeg"):
        with open(save_path+x, "rb")as opn:
            r=requests.post(url,files={"file":opn})
            print("process done")


if __name__ =="__main__":
    save_path=os.getcwd()+"/supplier-data/images/"
    url="http://localhost/upload/"
    items=os.listdir(save_path)
    n=len(items)
    pool=Pool(n)
    pool.map(image_upload, items)
    pool.close()

