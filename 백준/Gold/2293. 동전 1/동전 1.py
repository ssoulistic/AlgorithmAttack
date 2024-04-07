import sys
input=sys.stdin.readline
n,k=map(int,input().split())
dp=[0 for _ in range(k+1)]
coins=[]
for i in range(n):
    coins.append(int(input()))

coins.sort()
dp[0]=1

for coin in coins:
    for sum_value in range(coin,k+1):
        if sum_value-coin>=0:
            dp[sum_value]+=dp[sum_value-coin]
print(dp[k])
    