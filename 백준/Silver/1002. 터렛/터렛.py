import sys
T=int(sys.stdin.readline())
for _ in range(T):
    x1,y1,r1,x2,y2,r2=map(int,sys.stdin.readline().split())
    if x1==x2 and y1==y2:
        if r1==r2:
            print(-1)
        else:
            print(0)
    elif (x2-x1)**2+(y2-y1)**2==(r1+r2)**2 or (x2-x1)**2+(y2-y1)**2==(r1-r2)**2:
        print(1)
    elif (r1-r2)**2<(x2-x1)**2+(y2-y1)**2<(r1+r2)**2:
        print(2)
    else:
        print(0)