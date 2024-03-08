def solution(N, stages):
    users=len(stages)
    clear=[0 for _ in range(N+1)]
    ratio=[]
    for s in stages:
        clear[s-1]+=1
    for c in range(N):
        if users:
            ratio.append([-clear[c]/users,c])
            users-=clear[c]
        else:
            ratio.append([0,c])
    ratio=list(map(lambda x: x[1]+1,sorted(ratio)))
    return ratio