from itertools import permutations

perm=permutations('adil')

b=[]
d={}

for i in list(perm):
    b.append(''.join(i))

b

from random import randint
for i in b:
    d[i]=randint(-1000,1000)

d

balance=0

class Que:
    def __init__(self):
        self.qlist=[]
    def isEmpty(self):
        return len(self)==0
    def __len__(self):
        return len(self.qlist)
    def enque(self,item):
        self.qlist.append(item)
            
            
    def deque(self):
        assert not self.isEmpty()
        return self.qlist.pop(0)

q=Que()


for values in d.items():
    
    q.enque(values)

n=0
while True:
    n+=1
    p=q.deque()
    balance=balance+p[1]
    if balance<0:
        n=n-1
        break

for values in d.items():
    print(values)
    n-=1
    if n==0:
        break