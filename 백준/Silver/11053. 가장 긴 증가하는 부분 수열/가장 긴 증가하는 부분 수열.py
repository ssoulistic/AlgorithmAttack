T=int(input())
seq=list(map(int,input().split()))
lg=[1 for _ in range(T)]
for i in range(T):
    for j in range(i+1,T):
        if seq[i]<seq[j]:
            lg[j]=max(lg[j],lg[i]+1)
print(max(lg))