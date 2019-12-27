import sys
sys.path.append('/home/user/Desktop/task/week 1/utility')

from utility import temp_conversion
t=int(input('enter the temp'))
s=str(input('enter 1 to Celsius_to_Fahrenheit \n enter 2 to Fahrenheit_to_Celsius'))
(temp_conversion(t,s))