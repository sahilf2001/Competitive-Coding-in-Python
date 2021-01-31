# 24 [1,2,3,4,6,8,12,24]
# 32 [1,2,4,8,16,32]
# 30 [1,2,3,5,6,10,15,30]

from math import *

def fun1(n):
    # T.C = O(n)
    div1 = []
    for i in range(1,n+1):
        if(n%i==0):
            div1.append(i)
    return div1

def fun2(n):
    # T.C = O(root n)
    div2 = set()
    for i in range(1,int(sqrt(n))+1): #[1,root(n)]
        if(n%i==0):
            div2.add(i)
            div2.add(n//i)
    return list(div2)

t = int(input())
while t:
    n = int(input())
    div1 = fun1(n)
    div2 = fun2(n)
    print("The value from fun1() is:",div1)
    print("The value from fun2() is:", div2)
    t-=1

# O(n) > O(srt(n))
# Thus efficient algo is fun2()
