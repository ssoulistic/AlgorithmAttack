from itertools import product
n,m=map(int,input().split())
for i in product(list(range(1,n+1)),repeat=m):
    print(*i)