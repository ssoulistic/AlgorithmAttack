n=int(input())
topsell=dict()
for _ in range(n):
    sold=input()
    if topsell.get(sold):
        topsell[sold]+=1
    else:
        topsell[sold]=1
print(sorted(topsell.items(),key=lambda x: (-x[1],x[0]))[0][0])