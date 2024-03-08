import sys
input=sys.stdin.readline
N=int(input())
# 연속된 소수의 합
# 1. 소수 구하기 N까지
prime=[True for _ in range(N+1)]
prime[0]=False
prime[1]=False

def isPrime(num):
    for i in range(2,int(num**0.5)+1):
        if num % i==0:
            return False
    return True

for j in range(2,N+1):
    if isPrime(j) :
        prime[j]=True
        k=j
        k+=j
        while k<N+1:
            prime[k]=False
            k+=j

pool=[0]
for p in range(N+1):
    if prime[p]:
        pool.append(pool[-1]+p)
# 2. 소수 리스트에서 투포인터로 같은값 구하기.
# 3. 경우의 수 세서 출력
s=0
e=1
answer=0
while s<=e and e<len(pool):
    acc=pool[e]-pool[s]
    if acc==N:
        answer+=1
        e+=1
    elif acc<N:
        e+=1
    elif acc>N:
        s+=1
print(answer)