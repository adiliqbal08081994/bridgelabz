import sys
sys.path.append('/home/user/Desktop/task/week 1/utility')

from utility import gambler
stake=int(input('enter your stake'))
goal=int(input('enter your goal'))
n=int(input('how many times you want to play'))
gambler(stake,goal,n)



