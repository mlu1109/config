#!/usr/bin/python3
from subprocess import check_output

o = check_output(['sensors']).decode('utf-8')
print(o)