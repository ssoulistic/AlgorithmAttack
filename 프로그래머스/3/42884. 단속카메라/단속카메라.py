def solution(routes):
    routes.sort(key=lambda x: x[1])
    camera=-30001
    answer = 0
    for s,e in routes:
        if s<=camera<=e:
            continue
        elif camera<s:
            camera=e
            answer+=1
    return answer