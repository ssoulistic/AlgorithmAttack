T=int(input())
A=list(map(int,input().split()))
B=list()
answer=list(-1 for _ in range(T))
for i in range(T-1):
    B.append((A[i],i))
    while B and B[-1][0]<A[i+1]:
        answer[B.pop()[1]]=A[i+1]
print(*answer)