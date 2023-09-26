n=int(input())
got=set(input().split())
m=int(input())
have=input().split()
answer=[]
for num in have:
    if num in got:
        answer.append(1)
    else:
        answer.append(0)
print(*answer)