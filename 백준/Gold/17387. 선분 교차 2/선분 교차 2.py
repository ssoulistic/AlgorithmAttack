import sys
input=sys.stdin.readline
x1,y1,x2,y2=map(int,input().split())
x3,y3,x4,y4=map(int,input().split())

def ccw(p1,p2,p3):
    return (p2[0]-p1[0])*(p3[1]-p1[1])-(p2[1]-p1[1])*(p3[0]-p1[0])
A=[x1,y1]
B=[x2,y2]
C=[x3,y3]
D=[x4,y4]
if A>B:
    A,B=B,A
if C>D:
    C,D=D,C
if ccw(A,B,C)*ccw(A,B,D)<=0 and ccw(C,D,A)*ccw(C,D,B)<=0 and A<=D and B>=C:
    print(1)
else:
    print(0)
