#!/usr/bin/python3
import os
import subprocess
import requests
import wget

c = requests.get('http://dilbert.com/').content.decode('utf-8')
f = c.find('http://assets.amuniversal.com/')
t = c[f:].find('"')
FILE_NAME = wget.download(c[f:f+t], bar=False)
subprocess.call(['hsetroot', '-center', FILE_NAME])
os.remove(FILE_NAME)
