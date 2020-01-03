import sys
sys.path.append('/home/user/Desktop/task/week 2/utility')

from utility import sortedlist

import random

Start = 9
Stop = 99
limit = 10

b = [random.randrange(Start, Stop) for iter in range(limit)]
s=sortedlist()
for i in b:
    s.__sortlinkedlist__(i)

s.__display__()