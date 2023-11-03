N,K=map(int,input().split())
temp=list(map(int,input().split()))
answer=sum(temp[:K])
maxi=answer
for i in range(N-K):
    answer=answer-temp[i]+temp[i+K]
    if maxi<answer:
        maxi=answer
    
print(maxi)