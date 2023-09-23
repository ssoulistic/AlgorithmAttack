x=int(input())
answer=0
for i in range(x//2,x):
    parsum=i
    for j in str(i):
        parsum+=int(j)
    if parsum==x:
        answer=i
        break
print(answer)