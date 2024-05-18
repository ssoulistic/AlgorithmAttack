def solution(n, costs):
    def find(x):
        if group[x]!=x:
            group[x]=find(group[x])
        return group[x]
    def union(a,b):
        a=find(a)
        b=find(b)
        if a>b:
            group[a]=b
            return True
        elif a<b:
            group[b]=a
            return True
        return False
    
    costs.sort(key=lambda x: -x[2])
    group=[i for i in range(n)]
    answer = 0
    while costs:
        x,y,val=costs.pop()
        if union(x,y):
            answer+=val
    return answer