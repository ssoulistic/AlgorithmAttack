N,K=map(int,input().split())
last=0
count=0
for xi in map(int,input().split()):
    if last<xi:
        last=xi+K
        count+=1
print(count)
