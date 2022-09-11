import os
import sys

grouplist = open(sys.argv[2]).readlines()
grouplists = [w.replace('\n', '') for w in grouplist]
grouplistformated = (','.join(grouplists))
with open(sys.argv[1], "r") as f:
    for line in f:
        username = line.rstrip('\n')
        os.system("usermod -a -G %s %s" % (grouplistformated, username))