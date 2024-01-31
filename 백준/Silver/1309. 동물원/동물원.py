import sys
input=sys.stdin.readline
N=int(input())
dp=[[0,0,0] for _ in range(N)] # 0=> 배치하지 않는경우 1 왼쪽에만 배치 2 오른쪽에 배치
for i in range(3):
    dp[0][i]=1
for j in range(N-1):
    dp[j+1][0]=(dp[j][0]+dp[j][1]+dp[j][2])%9901
    dp[j+1][1]=(dp[j][0]+dp[j][2])%9901
    dp[j+1][2]=(dp[j][0]+dp[j][1])%9901
print(sum(dp[-1])%9901)
