import sys
sys.path.append('/home/user/Desktop/task/week 1/utility')

from utility import WindChill
temp=int(input('enter temp'))
vel=int(input('enter velocity'))
if abs(temp)<=50 and vel>3 and vel<=120:
    print(WindChill(temp,vel))
else:
    print('the formula is not valid for above val')


    