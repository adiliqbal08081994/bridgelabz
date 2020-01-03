import sys
sys.path.append('/home/user/Desktop/task/week 2/utility')

from utility import Stack
x=input('enter your expression')
s=Stack()
for i in x:
    if i=='(':
        s.push(i)
    elif i==')':
        s.pop()

        
if s.isEmpty()==True:
    print('balanced parantheses')
        