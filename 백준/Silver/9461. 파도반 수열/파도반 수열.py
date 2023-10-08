m=int(input())
tri=[1,1,1,2,2]+[0 for _ in range(95)]
def spiral(n):
    if n>=6:
        for i in range(5,n):
            tri[i]=tri[i-1]+tri[i-5]
    return tri[n-1]
for _ in range(m):
    x=int(input())
    print(spiral(x))