# n = 5
# 1+2+3+4+5 = 15
# n = 10
# 1+2+3+4+5+6+7+8+9+10 = 55

def sum1(m):
    # O(1)
    return (m)*(m+1)//2

def sum2(m):
    # O(n)
    sm = 0
    for i in range(1,m+1): #[1,m]
        sm+=i
    return sm

# O(n) > O(1)
# O(1) is a efficient program

t = int(input())
while t:
    n = int(input())
    print("sum1 executed output {}".format(sum1(n)))
    print("sum2 executed output {}".format(sum2(n)))
    t=t-1