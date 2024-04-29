import sys
input=sys.stdin.readline
C,N=map(int,input().split()) # 최소 확보 고객수 C명. N = 도시의 개수
dp=[[0 for _ in range(N)] for _ in range(C)]
for case in range(N):
    cost,gain=map(int,input().split())
    for total in range(C):
        if case==0:
            dp[total][case]=(total//gain+1)*cost
        else:
            if total-gain>=0:
                dp[total][case]=min(dp[total-gain][case]+cost,dp[total][case-1])
            else:
                dp[total][case]=min(dp[total][case-1],(total//gain+1)*cost)
    
print(dp[C-1][N-1])