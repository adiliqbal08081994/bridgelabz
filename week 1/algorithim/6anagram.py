import sys
sys.path.append('/home/user/Desktop/task/week 1/utility')

from utility import anagram
a=list(input('enter first word'))
b=list(input('enter second word'))
print(anagram(a,b))