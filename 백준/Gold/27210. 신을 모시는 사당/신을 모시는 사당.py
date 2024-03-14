import sys
input=sys.stdin.readline
N=int(input())
dol=list(map(int,input().split()))
# n번째 석상을 칠했을때, n-1번째 석상까지  칠한 왼쪽의 최대값+1(n이 왼쪽) 오른쪽의 최대값(n이 오른쪽 ).
dp=[[0,0] for _ in range(N+1)]
for i in range(N):
    if dol[i]==1:
        dp[i+1][0]=max(dp[i][0]+1,0)
        dp[i+1][1]=max(dp[i][1]-1,0)
    elif dol[i]==2:
        dp[i+1][0]=max(dp[i][0]-1,0)
        dp[i+1][1]=max(dp[i][1]+1,0)
answer=0
for x,y in dp:
    maximum=max(x,y)
    if maximum>answer:
        answer=maximum
print(answer)
        