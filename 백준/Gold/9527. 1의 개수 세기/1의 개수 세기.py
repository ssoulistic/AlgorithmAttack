import sys
input=sys.stdin.readline
A,B=map(int,input().split())
dp=[0 for _ in range(64)]
dp[0]=1
for i in range(len(dp)-1):
    dp[i+1]=2*dp[i]+2**(i+1)

def acc_one(given,acc):
    if given<=1:
        return given+acc
    bin_num=bin(given)
    next=int(bin_num[3:],2)
    acc+=next+1
    acc+=dp[len(bin_num)-4]
    return acc_one(next,acc)
print(acc_one(B,0)-acc_one(A-1,0))