import sys
import env
from lib.dice import *

try:
    sides = int(sys.argv[1])
except:
    sides = 6

try:
    times = int(sys.argv[2])
except:
    times = 10

d = dice(sides)

print d.sides

print d.roll(times)
