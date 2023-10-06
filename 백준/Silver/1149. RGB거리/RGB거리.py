# R G B 집 N개 1~N
# N !=N-1처럼 옆집과는 다름..
n=int(input())
dp=[[0,0,0] for _ in range(n)] #i번째 집을 j색으로 칠하는 최소비용.
colors=[]
for _ in range(n):
    colors.append(list(map(int,input().split())))
dp[0][0]=colors[0][0]
dp[0][1]=colors[0][1]
dp[0][2]=colors[0][2]

for i in range(1,n):
    dp[i][0] = min(dp[i-1][1],dp[i-1][2])+colors[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2])+colors[i][1]
    dp[i][2] = min(dp[i-1][0],dp[i-1][1])+colors[i][2]
print(min(dp[n-1]))