T=int(input())
lt=[]
for i in range(T):
    lt.append(tuple(map(int,input().split())))

for st in lt:
    rank=1
    for heavy in lt:
        if st[0]<heavy[0] and st[1]<heavy[1]:
            rank+=1
    print(rank)