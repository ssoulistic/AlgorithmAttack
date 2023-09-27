n,m=map(int,input().split())
dic=dict()
answer=0
for _ in range(n):
    dic[input()]=1
for _ in range(m):
    x=input()
    if dic.get(x):
        answer+=1
print(answer)