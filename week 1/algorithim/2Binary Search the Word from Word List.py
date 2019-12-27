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
            

print(d)