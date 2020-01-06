def prime(a,b):
    c=[]
    
    for num in range(a,b + 1):  
        if num > 1:  
            for i in range(2,num):  
                if (num % i) == 0:  
                    break  
            else:  
                c.append(num)  
    return c
d=list(range(0,1000,100))
e=[]
for i in range(len(d)-1):
    e.append(prime(d[i],d[i+1]))


print(e)