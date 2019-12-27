
import datetime
import math
import sys
import numpy as np
import random
import pandas as pd
# CoinToss function is created to count number of heads and tails
def CoinToss(toss):
    """
    :param toss: no of flips
    :return: no of head and tails
    """
    head = 0
    tail = 0
    try:  # try is used for locating the error
        for i in range(toss):
            flip = np.random.randint(0, 2)  # random function is used for 0 and 1 output
            if flip == 0:
                head += 1
            elif flip == 1:
                tail += 1
    except IndexError:
        print("index error please check ")
        # percentage of head and tail is counted by below functions
    percentageofhead = head / toss
    percentageoftail = tail / toss
    print("total number of head and tails are ", percentageofhead, percentageoftail)




# leap year function is created
def LeapYear(year):
    """
    :param year: year is taken as input
    :return: year is return if its leap year
    """
    # if input is not in yyyy then this loop will interrupt
    if len(str(year)) <= 3:
        print("plz enter year in yyyy format")
    elif len(str(year)) > 4:
        print("plz enter year in yyyy format")
        return
    # if condition is used for checking leap years
    elif (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("year is a leap year")
            else:
                print("year is not a leap year")
        else:
            print("year is a leap year")
    else:
        print("year is not a leap year")


# power of 2 function is used
def PowerOf2(num):
    """
    :param num: here num is taken as input
    :return: multiplied value of 2 is given
    """
    # for loop is used multiplication
    final= 2**num
    # final value is return
    return final




# harmonic function is used for calculating 1/n
def HarmonicValue(number):
    """
    :param number: number where we have to calculate harmonic function
    :return:
    """
    count = 0
    # for loop is used for calculating harmonic function
    for i in range(1, number + 1):  # for loop fot nth number
        add = 1 / i
        count += add
    # finally count is printed out
    print(count)
    return count


# prime factors is used for finding factors
def PrimeFactors(number):
    """
    :param number: number is entered to find prime factors
    :return: prime factors
    """
    while number % 2 == 0:
        print(2)  # 2 prime number is printed
        number = number / 2
    # for loop is used for finding factors
    for i in range(3, int(math.sqrt(number)) + 1, 2):  # for loop is used for finding factors
        while number % i == 0:
            print(i)
            number = number / i
    # here if condition is used if number is more than 2 then print
    if number >= 2:  # condition is used if prime number is greater than 2 is printed
        print(number)





def Array2d(row, col):
    """
    :param row: no of row
    :param col: no of col
    :return: 2d array
    """
    try:  # try is used for locating the error
        array = [[[np.random.randint(0, 10)] for i in range(row)] for j in range(col)]  # array is created by this
        # function
        print(array)
        return array  # array is returned
    except IndexError:
        print("index error please check ")


def Sum(num1, num2, num3):
    """
    :param num1: input of num1 is taken
    :param num2: input of num2 is taken
    :param num3: input of num3 is taken
    :return: sum of all the input is checked is zero or not
    """
    if num1 + num2 + num3 == 0:
        
        return True
    else:
        
        return False

# Distance is used for finding distance between 2 points

def Distance(x, y):
    """
    :param x: point 1
    :param y: point 2
    :return:  distance between 2 point
    """

    diff = ((x ** 2 + y ** 2))**.5
    
    # here difference is returned
    return diff


# Quad function is created
def Quad(num1, num2, num3):
    """
    :param num1: number 1 taken as input
    :param num2: number 2 taken as input
    :param num3: number 3 taken as input
    :return: after calculating quad results are returned
    """
    delta = num2 * num2 - 4 * num1 * num3
    if delta<0:
        print('you have imaginary roots')
    # have to convert -ve delta to +ve ,as -ve val does not have square roots
    print(abs(delta))
    root1 = (-num2 +(abs(delta))**.5) / (2 * num1)
    root2 = (-num2 -(abs(delta))**.5) / (2 * num1)
    
  
    # roots are returned
    return root1, root2



# wind chill function is created to check the input
def WindChill(temp, velocity):
    """
    :param temp: temp input is taken
    :param velocity:  velocity input is taken
    :return:
    """
    power = math.pow(velocity, 0.6)
    total = 35.47 + 0.6215 * temp + (0.4275 * temp + 35.75) * power
    # total function is used for the calculation

    return total


#gambler
def gambler(stake,goal,n):
    b=[]
    c=0
    t=stake
    d=0
    for i in range(n):
        win = 0
        while True:
            d=d+1
            win=random.randint(0,1)
            #print(win)
            if win==1:
                stake=stake+1
                c=c+1
                if stake==goal:
                    break
            else:
                stake=stake-1
                if stake==0:
                    break
        #print(stake)
        b.append(stake)
    #print(b)
    print(f'win percentage =  {(c/d)*100}')
    print(f'loose percentage =  {(1-(c/d))*100}')



#coupan
def Coupan(n):
    x=9
    c=1
    while True:
        if x<n:
            x=x*10
            c=c+1
        else:
            break
    def coupan(c,n):
        return(random.sample(range(10**c,(10**(c+1))),n))
    print(coupan(c,n))





# stopwatch
def StopWatch():
    """
    :return: time in sec is returned if pressed enter
    """
    start = datetime.datetime.now()
    if input("plz enter to stop the program "):
        return
    end = datetime.datetime.now()
    # prints time lapse
    print(abs(end - start))


#vending machine
def vending_machine(amt):
    
    l=[1000,500,100,50,10,2,1]
    a={}

    for i in l:
        a[i]=(amt//i)
        amt=amt%i
        

    print(f'total no of notes is {sum(a.values())}')
    print(a)



#day of week
def day_of_week(y,m,d):
    y0 = y - (14 - m) // 12
    x = y0 + y0//4 - y0//100 + y0//400
    m0 = m + 12* x* ((14 - m) // 12) - 2
    d0 = (d + x + 31*m0 / 12) % 7
    print(int(d0))




#temp conversion
def temp_conversion(t,s):
    if s=='1':
        def Celsius_to_Fahrenheit(t):
            return (int(t) * 9/5) + 32
        print(Celsius_to_Fahrenheit(t))
    else:
        def Fahrenheit_to_Celsius(t):
            return (int(t) - 32) * 5/9
        print(Fahrenheit_to_Celsius(t))



#monthly payment
def monthlyPayment(p,y,r):
	n=12*y
	R=r/(12*100)
	return p*R/(1-(1+R)**(-n))



#calculate square by newton method
def newtonsqr(a):
    x=1
    for i in range(100):
    
        f=(x**2 - a)
        f1=(2*x)
        x = x - f/f1
    return x


#convert number to binary
def to_binary(a):
	b=[]
	while a>=1:
		b.append(str(a%2))
		a=a//2
	b.reverse()
	s=''
	s=s.join(b)
	return int(s)
#decimal of swaped binary nibbles
def binarynibble(n):
    x=to_binary(n)
    x=str(x)
    x='0'*(8-len(x)%8)+x #this is original binary
    a=len(x)/2
    a=int(a)
    c=[x[:a],x[a:]]
    c[0],c[1]=c[1],c[0]
    
    s=''
    s=s.join(c)#this is after swap of nibbles
    q=0
    i=0
    t=len(s)-1
    while t>=0:
        q= q+(2**t)*int(s[i])
        i=i+1
        t=t-1
    return(q)


#permutation
def permutations(string, step = 0):
    if step == len(string):
        
        print ("".join(string))
    
    for i in range(step, len(string)):
        
        string_copy = [c for c in string]
         
        string_copy[step], string_copy[i] =string_copy[i], string_copy[step]
         
        permutations(string_copy, step + 1)
    return ' '


#insertion sort
def insertion_sort(l):

    a=[]
    def insertion(i):
        n=0
        if len(a)==0:
            a.append(i)
        else:
            
            for e in range(len(a)-1,-1,-1):
                if i>=a[e]:
                    a.insert(e+1,i)
                    break
                else:
                    n=n+1
                
        if n==len(a):
            a.insert(0,i)
    for i in l:
        insertion(i)
    print(a)



#bubble sort
def Bubble(l):
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]
    return(l)




# merge sort is used for sorting list
def Merge_Sort(llist):
    """
    :param llist: unsorted list is used
    :return: sorted list is returned
    """
    MergeSort2(llist, 0, len(llist) - 1)
    # merge sort second function is called


def MergeSort2(llist, first, last):
    """
    :param llist: unsorted list is used
    :param first: first half of the list
    :param last:  second half of the list
    :return: sorted list
    """
    try:
        if first < last:  # for loop is used for sorting the data
            middle = (first + last) // 2
            MergeSort2(llist, first, middle)
            MergeSort2(llist, middle + 1, last)
            Merge(llist, first, middle, last)
    except IndexError:
        print("index error ")

def Merge(llist, first, middle, last):
    """
    :param llist: unsorted list is used
    :param first: first half of the lsit
    :param middle: middle of the list
    :param last: last half of the list
    :return: sorted list
    """
    # list is divided in many 3 parts below
    left = llist[first:middle + 1]
    right = llist[middle + 1:last + 1]
    left.append(sys.maxsize)
    right.append(sys.maxsize)
    indexi = indexj = 0

    try:  # try is used for catch the error
        for k in range(first, last + 1):  # for loop is used for sorting the data
            if left[indexi] <= right[indexj]:
                llist[k] = left[indexi]
                indexi += 1
            else:
                # Comments
                llist[k] = right[indexj]
                indexj += 1
    except IndexError:  # error is found then below function is printed
        print("check for the index error")





#anagram detection
def anagram(a,b):

    a.sort()

    b.sort()

    print(a)
    print(b)

    c=b[b.index('a'):]
    return (a==c)



#prime numbers to range
def prime(z):
    p=[2,3,5]

    x=6
    n=3

    while x<z:
        t=1
        b=[]
        for i in p:
            r=x%i
            b.append(r)
        for i in b:
            t=t*i
        if t==0:
            x=x+1
        
        else:
            
            p.append(x)
            x=x+1
            n=n+1
        
    return(p)


#check anagram and palindrome of prime numbers
def primeanagram(z):
    p=prime(z)
    
    q=[]
    for i in range(len(p)):
        if str(p[i])==str(p[i])[-1::-1]:
            q.append(p[i])

    print(q)




#find your number
def find_your_number(n):
    N=2**n
    r=random.randint(0,N-1)

    print(f'your range is {N}')


    def f(n):
        a=int(input(f'input {n}th guess '))
        if a==r:
            return f'yes number is {r}'
        elif a>r:
            print(f'number is less than {a}')
        else:
            print(f'number is greater than {a}')
        if n==0:
            return f'not found actual number was {r}'
        return f(n-1)
        

    return f(n)