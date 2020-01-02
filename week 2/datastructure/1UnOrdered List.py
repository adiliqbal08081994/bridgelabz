import sys
sys.path.append('/home/user/Desktop/task/week 2/utility')

from utility import Bag
path='/home/user/Desktop/text2.txt'
x=open(path,'r')
x=x.read()
x=x.split(' ' or '/n')
linkedlist=Bag()
for i in x:
    linkedlist.__append__(i)
string=input('enter a text to search')
if linkedlist.__contains__(string)==True:
    linkedlist.remove(string)
else :
    linkedlist.__append__(string)

t=list(linkedlist.__elements__())

with open('/home/user/Desktop/text3.txt', 'w') as f:
    for i in range(len(t)-1,-1,-1):
        f.write(f' {t[i]}')
