import sys
T=int(sys.stdin.readline())
p=1000000007
last=0
def make_table(n,saved):
    if n==0 or n==1:
        return
    for i in range(saved,n):
        dp[i+1]=dp[i]*(i+1) % p    
    return n

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
dp=[1 for _ in range(4000001)]
for _ in range(T):
    N,K=map(int,sys.stdin.readline().split())
    if dp[N]==1:
        last=make_table(N,last)
    print((dp[N]*divnum(dp[K]*dp[N-K],p-2))%p)