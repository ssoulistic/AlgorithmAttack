import sys
input=sys.stdin.readline
t=int(input())
acc=1
for i in range(1,t+1):
    acc*=i
print(acc)
    