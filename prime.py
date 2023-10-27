import math

def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i ==0:
            return 0
    return 1

n = int(input())

i=2

while i <= n:
    if isPrime(i):
        print(i)
        i +=1
    else: i+=1

