import sys
sys.path.append('/home/user/Desktop/task/week 1/utility')

from utility import Quad
a=int(input('enter coefficient of x^2 '))
b=int(input('enter coefficient of x'))
c=int(input('enter coefficient of c'))
print(Quad(a,b,c))
