import requests
import json
import re
import time
import random

get_line = sum([1 for _ in open('id.txt')])
    
def get_text(file_name, line_number):
    with open(file_name) as f:
        for i, line in enumerate(f, 1):
            if i == line_number:
                return line.rstrip('\n')

def check():
    data = {
        'username': id,
    }
    req = requests.post("https://misskey.io/api/username/available", json = data)
    data = req.json()["available"]
    if data==True:
        print("avaible " + id)
        f = open('avaible.txt', 'a')
        f.writelines(f"{id}\n")
        f.close
    else:
        print("not avaible " + id)

counter = get_line
while counter > 0:
    time.sleep(random.uniform(0.25, 0.35))
    id = str(get_text('id.txt', counter))
    check()
    counter = counter - 1