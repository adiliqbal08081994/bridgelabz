import sys
sys.path.append('/home/user/Desktop/task/week 1/utility')

from utility import Sum
from itertools import combinations
#x=list(input('enter the numbers'))
x=[-1,-2,0,1,2]
com=combinations(x,3)
b=[]
for i in list(com):
    b.append(i)
for i in b:
    if Sum(i[0],i[1],i[2])==True:
        print(i)