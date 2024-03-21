from itertools import combinations
def solution(orders, course):
    answer = []
    
    for c in course:
        dic={}
        for w1 in range(len(orders)):
            for combo in combinations(orders[w1],c):
                combo="".join(sorted(combo))
                for w2 in range(len(orders)):
                    if w1!=w2:
                        if all(True if k in orders[w2] else False for k in combo ):
                            if dic.get(combo):
                                dic[combo]+=1
                            else:
                                dic[combo]=1
        if dic:
            print(dic)
            print()
            maximum=max(dic.values())
            for k,v in dic.items():
                if v==maximum:
                    answer.append("".join(sorted(k)))
    return sorted(answer)