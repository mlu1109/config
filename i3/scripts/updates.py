#!/usr/bin/python3
from subprocess import check_output, call
from sys import argv

if 1 < len(argv) and argv[1] == '1':
  call(['x-terminal-emulator', '-e', 'apt list --upgradable'])
elif 1 < len(argv) and argv[1] == '3':
  cmd = 'sudo apt update'
  call(['x-terminal-emulator', '--title', cmd, '-e', cmd])

o = check_output(['apt', 'list', '--upgradable']).decode('utf-8')
u = o.count('upgradable')
if 0 < u:
  print("<span color='lime'> <b>%s</b></span>"% u)
else:
  print(" %s"% u)