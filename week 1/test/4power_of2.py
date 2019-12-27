import sys
sys.path.append('/home/user/Desktop/task/week 1/utility')

from utility import PowerOf2

while True:
    n=int(input('enter a number'))
    if n>=0 and n<31:
        break
    else:
        print('enter a val between 0-31')

for i in range(n+1):
    print(PowerOf2(i))