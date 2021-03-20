#!/usr/bin/python

# Curses radio via curses-menu
# pip install curses-menu

from cursesmenu import *
from cursesmenu.items import *

import subprocess
import time

player = 'mpv'



# ======= fill list of stations from index file =============
file = 'index'
stations = []
lines = sum(1 for line in open(file,'r'))

with open(file, 'r') as inf:
    i = 1
    while i <= lines:
        station = inf.readline().strip().split(' # ')
        stations.append(station)
        i += 1

# ======== Create menu ======================================
menu = CursesMenu("C U R S E S   R A D I O", "===== Choose station:")

for i in stations:
    menu.append_item(CommandItem(f'{i[0]}', f'{player} {i[1]}'))


menu.show()
