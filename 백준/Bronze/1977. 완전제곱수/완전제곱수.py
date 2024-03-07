import sys
input=sys.stdin.readline
M=int(input())
N=int(input())
acc=0
small=N
for i in range(int(M**0.5),int(N**0.5)+1):
    if M<=i**2<=N:
        acc+=i**2
        if small>i**2:
            small=i**2
if acc:
    print(acc)
    print(small)
else:
    print(-1)