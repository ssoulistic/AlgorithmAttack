n=int(input())
for i in map(int,input().split()):
    if i ==1:
        n-=1
        continue
    for j in range(2,i):
        if i % j ==0:
            n-=1
            break
print(n)