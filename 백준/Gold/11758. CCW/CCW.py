import sys
input=sys.stdin.readline
xp1,yp1=map(int,input().split())
xp2,yp2=map(int,input().split())
xp3,yp3=map(int,input().split())

# 1,2 를 지난 직선의 위 아래
a,b=(xp3-xp2,yp3-yp2)
c,d=(xp1-xp2,yp1-yp2)
det=a*d-b*c

if det>0:
    print(1)
elif det==0:
    print(0)
else:
    print(-1)