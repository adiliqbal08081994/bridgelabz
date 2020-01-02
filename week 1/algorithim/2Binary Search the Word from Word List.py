path='/home/user/Desktop/task/week 1/algorithim/text.txt'

x=open(path,'r')

x=x.read()

x=list(x)

for i in range(len(x)):
    if x[i]=='\n':
        x[i]=' '

s=''
x=s.join(x)
x=x.split(' ')

l=str(input('enter the words with comma'))

l=l.split(',')
print(l)

d={}

for i in range(len(l)):
    n=0
    for j in range(len(x)):
        
        if str(x[j])==l[i]:
            n=n+1
            d[l[i]]=n
            
def binnary_search(list1,target):
    low =0
    high=len(list1)-1
    while low<=high:
        mid= (high + low)//2
        if list1[mid]==target:
            return True
        elif target<list1[mid]:
            high=mid-1
        else:
            low=mid+1
    return False
for i in x:
    if binnary_search(l,x)==True:
        n=n+1
        d[i]

print(d)