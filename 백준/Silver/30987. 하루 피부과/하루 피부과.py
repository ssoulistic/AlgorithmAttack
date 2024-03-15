import sys
input=sys.stdin.readline
x1,x2=map(int,input().split())
a,b,c,d,e=map(int,input().split())
def laser(y):
    return a*(y**3)/3+(b-d)*(y**2)/2+(c-e)*y
print(int(laser(x2)-laser(x1)))