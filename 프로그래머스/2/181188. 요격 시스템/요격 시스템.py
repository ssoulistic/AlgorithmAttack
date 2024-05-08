def solution(targets):
    targets.sort(key= lambda x: x[1])
    shoot=-0.5
    answer = 0
    for s,e in targets:
        if shoot<s:
            shoot=e-0.5
            answer+=1
            
    return answer