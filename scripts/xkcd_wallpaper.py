#!/usr/bin/python3
import os
import subprocess
import requests
import wget

DAILY = 'https://xkcd.com'
RANDOM = 'https://c.xkcd.com/random/comic/'

c = requests.get(RANDOM).content.decode('utf-8')
f = c.find('imgs.xkcd.com/comics/')
t = c[f:].find('"')
FILE_NAME = wget.download('https://' + c[f:f+t], bar=False)
subprocess.call(['hsetroot', '-center', FILE_NAME])
os.remove(FILE_NAME)
