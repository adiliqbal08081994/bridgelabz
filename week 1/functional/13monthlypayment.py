import sys
sys.path.append('/home/user/Desktop/task/week 1/utility')

from utility import monthlyPayment
p=int(input('enter the principle amount'))
y=int(input('enter your time in years'))
r=int(input('enter your rate of intrest'))
print(monthlyPayment(p,y,r))
