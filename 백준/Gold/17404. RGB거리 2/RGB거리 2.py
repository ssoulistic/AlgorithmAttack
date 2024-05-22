import sys
input=sys.stdin.readline
N=int(input())
dp1=[[0,0,0] for _ in range(N)]
dp2=[[0,0,0] for _ in range(N)]
dp3=[[0,0,0] for _ in range(N)]
R,G,B=map(int,input().split())
dp1[0]=[R,1e9,1e9]
dp2[0]=[1e9,G,1e9]
dp3[0]=[1e9,1e9,B]
for i in range(1,N):
    R,G,B=map(int,input().split())
    dp1[i][0]=min(dp1[i-1][1],dp1[i-1][2])+R
    dp1[i][1]=min(dp1[i-1][0],dp1[i-1][2])+G
    dp1[i][2]=min(dp1[i-1][0],dp1[i-1][1])+B

    dp2[i][0]=min(dp2[i-1][1],dp2[i-1][2])+R
    dp2[i][1]=min(dp2[i-1][0],dp2[i-1][2])+G
    dp2[i][2]=min(dp2[i-1][0],dp2[i-1][1])+B

    dp3[i][0]=min(dp3[i-1][1],dp3[i-1][2])+R
    dp3[i][1]=min(dp3[i-1][0],dp3[i-1][2])+G
    dp3[i][2]=min(dp3[i-1][0],dp3[i-1][1])+B
print(min(dp1[N-1][1],dp1[N-1][2],dp2[N-1][0],dp2[N-1][2],dp3[N-1][0],dp3[N-1][1]))
# 1 2 3 번 하나씩
