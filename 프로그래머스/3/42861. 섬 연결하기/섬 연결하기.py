def solution(n, costs):
    # 간선 위주 => 크루스칼 알고리즘
    # 최소 비용의 간선순으로 사이클이 발생 하지 않도록 연결
    # 사이클 발생여부는 유니온 파인드로 확인.
    
    # 유니온 파인드 정의 구간
    group=[i for i in range(n)]
    def find(x):
        if group[x]!=x:
            group[x]=find(group[x])
        return group[x]
    
    def union(a,b):
        a,b=find(a),find(b)
        if a!=b:
            group[min(a,b)]=max(a,b)
            return True
        return False
    
    #deque 불러오기싫어서 역순으로 정렬
    answer = 0
    costs.sort(key=lambda x: -x[2])
    while costs:
        start,end,value=costs.pop()
        if union(start,end):
            answer+=value
    return answer