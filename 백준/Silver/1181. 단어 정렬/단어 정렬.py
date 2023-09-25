n=int(input())
l=[]
for _ in range(n):
    l.append(input())
l=sorted(set(l))
l.sort(key=len)
print(*l)