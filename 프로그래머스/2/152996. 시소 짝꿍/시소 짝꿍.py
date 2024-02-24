def solution(weights):
    # 1. 같은 쌍 세기.
    # 2. 다른 쌍 찾아 더하기.
    peo={}
    answer = 0
    heavy=sorted(set(weights))
    for w in heavy:
        peo[w]=weights.count(w)
    
    for p in peo.values():
        answer+= p*(p-1)//2
    
    for i in range(len(heavy)):
        for j in range(i+1,len(heavy)):
            if heavy[i]*3==heavy[j]*2 or heavy[i]*4==heavy[j]*2 or heavy[i]*4==heavy[j]*3:
                answer+=peo[heavy[i]]*peo[heavy[j]]
            elif heavy[i]*2<heavy[j]:
                break
    return answer