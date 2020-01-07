import numpy as np
def primeanagram(z):
    p=prime(z)
    
    q=[]
    for i in range(len(p)):
        if str(p[i])==str(p[i])[-1::-1]:
            q.append(p[i])

    print(q)

x=np.array(prime(1000))

y=[]
z=[]

for i in range(len(x)):
    c=0
    t=list(str(x[i]))
    t.sort()
    for j in range(len(x)-1,i,-1):
        u=list(str(x[j]))
        u.sort()
        if t==u:
            
            c=1
    if c==1:
        z.append(x[i])
    else:
        y.append(x[i])
        
final=np.array([y,z])
print(final)