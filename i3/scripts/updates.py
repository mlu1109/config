#!/usr/bin/python3
from subprocess import check_output, call
from sys import argv

if 1 < len(argv) and argv[1] == '1':
  call(['x-terminal-emulator', '-e', 'apt list --upgradable'])
elif 1 < len(argv) and argv[1] == '3':
  cmd = 'sudo apt update'
  call(['x-terminal-emulator', '--title', cmd, '-e', cmd])

str = check_output(['apt', 'list', '--upgradable']).decode('utf-8')
i = 0
u = 0
while True:
  i = str.find('upgradable', i, len(str))
  if i == -1:
    break
  i += 1
  u += 1

if 0 < u:
  print("<span color='lime'> <b>%s</b></span>"% u)
else:
  print("%s"% u)