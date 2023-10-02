def fac(m):
    res=1
    for l in range(1,m+1):
        res*=l
    return res

n=int(input())
for _ in range(n):
    j,k=map(int,input().split())
    print(fac(k)//(fac(j)*fac(k-j)))