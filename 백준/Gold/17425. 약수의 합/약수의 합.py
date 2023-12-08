import sys
F=[0]*1000001
G=[0]*1000001
answer=[]
for i in range(1,1000001):
    for j in range(i,1000001,i):
        F[j]+=i
for k in range(1,1000001):
    G[k]=G[k-1]+F[k]

T=int(sys.stdin.readline())
for _ in range(T):
    x=int(sys.stdin.readline())
    answer.append(str(G[x]))
print("\n".join(answer))
