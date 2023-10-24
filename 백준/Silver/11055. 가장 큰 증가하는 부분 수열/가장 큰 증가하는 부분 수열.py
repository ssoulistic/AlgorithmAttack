T=int(input())
seq=list(map(int,input().split()))
dp=seq.copy() # n번째까지의 최대합.
for i in range(T):
    for j in range(i+1,T):
        if seq[i]<seq[j]: # 증가하는 수열.
            dp[j]=max(dp[i]+seq[j],dp[j]) # 그 전에 기록된 수열의 합 dp[j] vs 새로운 수열의 합 dp[i]+seq[j]
print(max(dp))
