import psutil

from subprocess import Popen
# round(), GB 1024, 2de
# Importing the library
import psutil

# Getting % usage of virtual_memory ( 3rd field)
print('RAM memory % used:', psutil.virtual_memory()[2])