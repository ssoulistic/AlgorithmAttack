import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    n=int(input())
    sticker=[]
    answer=0
    dp=[[0 for _ in range(n)] for _ in range(3)]
    for _ in range(2):
        sticker.append(list(map(int,input().split())))
    sticker.append([0 for _ in range(n)])
    for j in range(3):
        dp[j][0]=sticker[j][0]
    for i in range(n-1):
        dp[0][i+1]=max(dp[1][i],dp[2][i])+sticker[0][i+1]
        dp[1][i+1]=max(dp[0][i],dp[2][i])+sticker[1][i+1]
        dp[2][i+1]=max(dp[0][i],dp[1][i])+sticker[2][i+1]
    for line in dp:
        if answer<line[-1]:
            answer=line[-1]
    print(answer)