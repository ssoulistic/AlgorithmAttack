import sys
input=sys.stdin.readline
H,W,N,M=map(int,input().split())
A=H//(N+1)
B=W//(M+1)
if H % (N+1):
    A+=1
if W % (M+1):
    B+=1
print(A*B)
