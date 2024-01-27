import sys
input=sys.stdin.readline
for _ in range(3):
    N=int(input())
    temp=0
    for _ in range(N):
        temp+=int(input())
    if temp<0:
        print("-")
    elif temp==0:
        print(0)
    else:
        print("+")