# -*- coding: utf-8 -*-

import json
from tkinter import *
import requests

def request():
  repoz = 'https://api.github.com/repos/NixOS/nixpkgs'
  data = requests.get(repoz).json()
  data = dict((key, data[key]) for key in ['company', 'created_at', 'email', 'id', 'name', 'url'] if key in data)
  with open('NetStrex.json', 'w') as file:
    json.dump(data, file)

window = Tk()
window.minsize(600, 800)
window.title('NetStrex')
Button(window, text='Get it!', command=request).pack()
window.mainloop()