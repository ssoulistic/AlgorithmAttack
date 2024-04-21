def solution(name):
    # 1. 다른 문자로 변형할때 누르는 수
    # 2. 바꿔야할 문자들을 찾아가는 최단 거리
    # 0에서 출발해서 어딘가를 거친 다음 반대쪽으로 가는 거리.
    # 연속된 목적지 2개..
    answer = 0
    targets=[0]
    results=[]
    for idx,alp in enumerate(name):
        answer+=min((ord(alp)-ord("A")),26-(ord(alp)-ord("A")))
        if alp!="A":
            targets.append(idx)
    results.append(min(max(targets),len(name)-min(targets)))
    # 움직임. 두 좌표
    cursor=0
    while cursor<len(targets):
        results.append(min(len(name)-targets[-cursor],targets[-cursor-1])*2+max(len(name)-targets[-cursor],targets[-cursor-1]))
        cursor+=1
    answer+=min(results)    
    return answer