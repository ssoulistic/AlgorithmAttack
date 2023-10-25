# 좌 우의 LCS 구하기. 합하기.
T=int(input())
seq=list(map(int,input().split()))
# 오름 내림 순서.
dp=[[1,1] for _ in range(T)]
for i in range(0,T):
    for j in range(i+1,T):
        if seq[i]<seq[j]:
            dp[j][0]=max(dp[i][0]+1,dp[j][0])
        if seq[T-i-1]<seq[T-j-1]:
            dp[T-j-1][1]=max(dp[T-i-1][1]+1,dp[T-j-1][1])
print(max(map(sum,dp))-1)    