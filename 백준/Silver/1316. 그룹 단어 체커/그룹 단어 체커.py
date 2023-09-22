n=int(input())
answer=0
for _ in range(n):
    x=input()
    y=x[0]
    for i in range(len(x)-1):
        if x[i]!=x[i+1]:
            y+=x[i+1]
    if len(y)==len(set(y)):
        answer+=1
print(answer)
