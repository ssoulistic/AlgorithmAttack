x,y=[],[]
for _ in range(int(input())):
    i,j=map(int,input().split())
    x.append(i)
    y.append(j)
if len(x)==1:
    print(0)
else:
    print((max(x)-min(x))*(max(y)-min(y)))