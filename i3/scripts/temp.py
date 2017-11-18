#!/usr/bin/python3
from subprocess import check_output, Popen, PIPE
import re
s = Popen(['sensors'], stdout=PIPE)
o = check_output(['grep', 'Core'], stdin=s.stdout).decode('utf-8').splitlines()
reg = re.compile('Core.+?(\+.+?)\s\m')

print(reg.match(o[0]).groups(0))