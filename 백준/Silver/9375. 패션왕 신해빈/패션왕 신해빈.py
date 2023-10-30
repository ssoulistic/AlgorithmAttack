T=int(input())
for _ in range(T):
    n=int(input())
    outfit=dict()
    answer=1
    for _ in range(n):
        cloth,tp=input().split()
        if outfit.get(tp):
            outfit[tp]+=1
        else:
            outfit[tp]=1
    for i in outfit.values():
        answer*=(i+1)
    print(answer-1)