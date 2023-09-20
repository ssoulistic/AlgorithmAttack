import math
m=int(input())
n=int(input())
primes=[]
isPrime=True
for i in range(m,n+1):
    if i==1:
        continue
    for j in range(2,int(math.sqrt(i))+1):
        if i % j ==0:
            isPrime=False
            break
    if isPrime:
        primes.append(i)
    isPrime=True
if primes:
    print(sum(primes))
    print(min(primes))
else:
    print(-1)
