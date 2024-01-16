import sys
input=sys.stdin.readline
N=int(input())
mindp=[[0,0,0] for _ in range(2)]
maxdp=[[0,0,0] for _ in range(2)]
for i in range(N):
    board=list(map(int,input().split()))
    if i ==0:
        mindp[i][0]=board[0]
        mindp[i][1]=board[1]
        mindp[i][2]=board[2]
        maxdp[i][0]=board[0]
        maxdp[i][1]=board[1]
        maxdp[i][2]=board[2]
    else:
        mindp[i%2][0]=min(mindp[(i-1)%2][0],mindp[(i-1)%2][1])+board[0]
        mindp[i%2][1]=min(mindp[(i-1)%2][0],mindp[(i-1)%2][1],mindp[(i-1)%2][2])+board[1]
        mindp[i%2][2]=min(mindp[(i-1)%2][1],mindp[(i-1)%2][2])+board[2]
        maxdp[i%2][0]=max(maxdp[(i-1)%2][0],maxdp[(i-1)%2][1])+board[0]
        maxdp[i%2][1]=max(maxdp[(i-1)%2][0],maxdp[(i-1)%2][1],maxdp[(i-1)%2][2])+board[1]
        maxdp[i%2][2]=max(maxdp[(i-1)%2][1],maxdp[(i-1)%2][2])+board[2]
print(max(maxdp[(N+1)%2]),min(mindp[(N+1)%2]))