import sys
n=int(sys.stdin.readline())
lev=[]
for _ in range(n):
    x=int(sys.stdin.readline())
    lev.append(x)
def rud(m):
    if m%1>=0.5:
        return int(m)+1
    else:
        return int(m)

lev.sort()
r=rud(len(lev)*0.15)
if lev:
    print(rud(sum(lev[r:len(lev)-r])/(len(lev)-2*r)))
else:
    print(0)
