import sys
sys.path.append('/home/user/Desktop/task/week 2/utility')

from utility import Deque
x=input('enter a string')
l1=Deque()
l2=Deque()
for i in x:
    l1.addLastItem(i)
    l2.addFrontItem(i)

t=1
while l1.__len__()>1 and l1.__len__()>1:
    a=l2.Delete_At_End()
    b=l1.Delete_At_End()
    if a!=b:
        t=0
    
        
if t==0:
    print("not a palindrome")
else:
    print('palindrome')