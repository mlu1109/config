#!/usr/bin/python3

# This is mainly a Python3 port of the script provided with i3blocks by the authors below.

# Uses ~/.bandwidth-{interface} for caching

# Copyright (C) 2012 Stefan Breunig <stefan+measure-net-speed@mathphys.fsk.uni-heidelberg.de>
# Copyright (C) 2014 kaueraal
# Copyright (C) 2015 Thiago Perrotta <perrotta dot thiago at poli dot ufrj dot br>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Use the provided interface, otherwise the device used for the default route.

import os
import subprocess
import sys
import time

interface = ''
cmd = ''
# Use the provided interface, otherwise the device used for the default route.
#if os.environ['BLOCK_INSTANCE']:
#  interface = os.environ['BLOCK_INSTANCE']
#else:
cmd = ['ip', 'route']
ip_route = subprocess.check_output(cmd).decode().split(' ')
interface = ip_route[ip_route.index('default') + 4]

# path to store the old results in
path = '{}/.cache/bandwidth-{}'.format(os.path.expanduser('~'), interface)

# grabbing data for each adapter.
cmd = ['cat', '/sys/class/net/{}/statistics/rx_bytes'.format(interface)]
rx = int(subprocess.check_output(cmd))
cmd = ['cat', '/sys/class/net/{}/statistics/tx_bytes'.format(interface)]
tx = int(subprocess.check_output(cmd))

# get time (s)
time = int(round(time.time()))

# write current data if file does not exist. Do not exit, this will cause
# problems if this file is sourced instead of executed as another process.
if (not os.path.isfile(path)):
  f = open(path, 'w')
  f.write('{} {} {}'.format(time, rx, tx))
  f.close()
  sys.exit(0)

# read previous state and update storage
f = open(path, 'r+')
old = f.read().split(' ')
f.seek(0)
f.truncate(0)
f.write('{} {} {}'.format(time, rx, tx))

# diffs
time_diff = time - int(old[0])
rx_diff = rx - int(old[1])
tx_diff = tx - int(old[2])

# rates
rx_rate = int(rx_diff / time_diff) >> 10 # KiB
tx_rate = int(tx_diff / time_diff) >> 10 # KiB

# output
rx_icon = ''
tx_icon = ''
rx_out = ''
tx_out = ''
if (rx_rate > 2**10):
  rx_out = '{:.1f}{}'.format(rx_rate / 1024, 'M')
else:
  rx_out = '{}{}'.format(rx_rate, 'K')

if (tx_rate > 2**20):
  tx_out = '{:.1f}{}'.format(tx_rate / 1024, 'M')
else:
  tx_out = '{}{}'.format(tx_rate, 'K')

# set color depending on speed
rgb_spread = (255-255, 255-0, 255-0)
rgb_rxf = min(rx_rate / 10000, 1)
rgb_txf = min(tx_rate / 10000, 1)

rxc = (255 - int(rgb_spread[0]*rgb_rxf), 255 - int(rgb_spread[1]*rgb_rxf), 255 - int(rgb_spread[2]*rgb_rxf))
txc = (255 - int(rgb_spread[0]*rgb_txf), 255 - int(rgb_spread[1]*rgb_txf), 255 - int(rgb_spread[2]*rgb_txf))
rx_color = '#{0:0{1}x}{2:0{1}x}{4:0{1}x}'.format(rxc[0], 2, rxc[1], 2, rxc[2], 2)
tx_color = '#{0:0{1}x}{2:0{1}x}{4:0{1}x}'.format(txc[0], 2, txc[1], 2, txc[2], 2)
print('<span color="{}">{} {}</span> <span color="{}">{} {}</span>'.format(rx_color, rx_icon, rx_out, tx_color, tx_icon, tx_out))
