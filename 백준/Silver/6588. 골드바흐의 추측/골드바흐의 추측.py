import sys
primenum=[1 for _ in range(1000001)]
primenum[0]=0
primenum[1]=0

for l in range(2,1000001):
    if primenum[l]:
        k=2
        while l*k<=1000000:
            primenum[l*k]=0
            k+=1

while True:
    n=int(sys.stdin.readline().strip())
    if n==0:
        break
    answer="Goldbach's conjecture is wrong."
    for j in range(3,n,2):
        if primenum[j] and primenum[n-j]:
            answer=(f"{n} = {j} + {n-j}")
            break
    print(answer)