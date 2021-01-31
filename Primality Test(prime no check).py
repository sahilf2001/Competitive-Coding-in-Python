from math import *

def prime(n):
    divcnt = 0
    for i in range(1,n+1):
        if n%i==0:
            divcnt+=1
    if(divcnt==2):
        return True
    else:
        return False

def prime1(n):
    if n==0 or n==1:
        return False
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    for i in range(5,int(sqrt(n))+1):
        if n%i==0 or n%(i+2) ==0:
            return False
    return True



t = int(input())
while t:
    n = int(input())
    if(prime1(n)):
        print("The number is prime...")
    else:
        print("The number is not prime...")
    t-=1