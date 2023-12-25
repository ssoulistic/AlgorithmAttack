N,K=map(int,input().split())
dp=[1 for _ in range(N+1)]
p=1000000007

for i in range(1,N):
    dp[i+1]=dp[i]*(i+1) % p
A=dp[N]
B=(dp[K]*dp[N-K])

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

print((dp[N]*divnum(dp[K]*dp[N-K],p-2))%p)