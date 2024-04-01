import sys
input=sys.stdin.readline
E,S,M=map(int,input().split())
x=0
while True:
    if ((E-S)+15*x) % 28==0 and ((E-M)+15*x)% 19==0:
        break
    x+=1
print((E-1)+15*x+1)
    