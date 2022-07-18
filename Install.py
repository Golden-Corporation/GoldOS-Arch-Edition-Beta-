import os
import time

input('Start installing? ')
print('Installing.')
print('Please wait for a little while, while we prepare.')
print('If you see anything about a lock, please reboot your computer.')

time.sleep(3)

os.system('sudo pacman -Syu') # Always run this first, can fix broken installs.

os.system('sudo pacman -S install plymouth-themes')
os.system('sudo pacman -S install python3-tk')
os.system('sudo pacman -S install git')

print('\nFinishing up.')

os.system('python3 Start2.py')
