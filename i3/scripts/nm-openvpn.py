#!/usr/bin/python3
from subprocess import check_output

connected = False
name =  ''

o = check_output(['nmcli', 'connection']).decode('utf-8')
for line in o.splitlines():
  parts = line.split()
  i = len(parts) - 3 # Name can have spaces
  if parts[i + 1].lower() == 'vpn' and parts[i + 2] != '--':
    name = ' '.join(parts[:i])
  elif parts[i + 1].lower() == 'tun' and parts[i + 2] != '--':
    connected = True

if connected:
  print('VPN: %s'% name)
elif name: # Connecting
  print('<span color="yellow">VPN: ...</span>')
else:
  print('<span color="red">VPN: DOWN</span>')