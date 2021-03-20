#!/usr/bin/python
import subprocess
import time

player = 'mpv'

# fill list of stations from index file
file = 'index'
stations = []
lines = sum(1 for line in open(file,'r'))

with open(file, 'r') as inf:
    i = 1
    while i <= lines:
        station = inf.readline().strip().split(' # ')
        stations.append(station)
        i += 1
        
        
# start menu
def start_menu():
    for i in range(len(stations)):
        print(f'{i} - {stations[i][0]}')
    print('q - quit()')

# user press number of station or quit
def choice(n):
    if n == 'q':
        quit()    
    else:
        station = stations[int(n)][1]
    return station
    
# switch station
def switch(n):
    return subprocess.Popen([player, n], stdout=subprocess.DEVNULL, stderr = subprocess.DEVNULL)

while True:
    start_menu()
    n = input()
    play = switch(choice(n))
    time.sleep(5)
    print('press q to exit from station')
    print('pres  Q to quit from program')
    n = input()
    if n == 'q':
        play.kill()
    if n == 'Q':
        play.kill()
        break
