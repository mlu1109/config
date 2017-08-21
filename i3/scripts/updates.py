#!/usr/bin/python3

# To make this script able to update the list of packages:
# ----------------------------------
# sudo chown root.root <this-script>
# sudo chmod 4755 <this-script> 
# ----------------------------------
# This makes the file exectubale by all but only wrtiable by root.

from subprocess import check_output, call
from sys import argv

if 1 < len(argv) and argv[1] == '1':
  call(['x-terminal-emulator', '-e', 'apt list --upgradable'])

call(['sudo', 'apt update'])

o = check_output(['apt', 'list', '--upgradable']).decode('utf-8')
u = o.count('upgradable')
if 0 < u:
  print("<span color='lime'> <b>%s</b></span>"% u)
else:
  print(" %s"% u)