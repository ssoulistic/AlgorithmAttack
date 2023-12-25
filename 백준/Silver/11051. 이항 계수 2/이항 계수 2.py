import sys
sys.setrecursionlimit(10**6)
N,K=map(int,input().split())
dp=[1 for _ in range(N+1)]
p=10007

def factorial(n):
    if n==0 or n==1:
        return dp[n]
    if dp[n]==1:
        dp[n]=n*factorial(n-1)
    return dp[n]

A=factorial(N) % p
B=(factorial(K)*factorial(N-K)) % p

def divnum(n,repeat):
    number=1
    count=0
    while count<repeat:
        number*=n
        count+=1
        over,left=divmod(number,p)
        if over:
            skip,left2 =divmod(repeat,count)
            return (divnum(left,skip)*(n**left2)) % p
    return left

print((A*divnum(B,p-2))%p)
