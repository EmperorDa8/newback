#!/usr/bin/env python3
import os , datetime
from reports import generate_report
import emails

current_date=datetime.datetime.now().strftime('%y-%m-$d')

def generate_raw(path):
    pdf_file=""
    for item in os.listdir(path):
        if item.endswith(".txt"):
            with open(item)as f:
            lines= f.readlines()
            name=lines[0].strip()
            weight=lines[1].strip()
            pdf=pdf_file+"Name>>"+name+"<br/>"+"weight>>"+weight+"<br/><br/>"
    return pdf


if __name__ == "__main__":
    path="supplier_data/descriptions/"
    title="process updated on"+ current_date
    #pdf generate
    content=generate_raw(path)
    generate_report("/tmp/processed.pdf",title,content)

