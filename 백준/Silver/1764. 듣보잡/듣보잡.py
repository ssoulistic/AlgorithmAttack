n,m=map(int,input().split())
whoareu={}
answer=[]
for _ in range(n):
    whoareu[input()]=1
for _ in range(m):
    x = input()
    if whoareu.get(x):
        answer.append(x)
print(len(answer))
for i in sorted(answer):
    print(i)