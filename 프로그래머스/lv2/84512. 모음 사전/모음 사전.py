def solution(word):
    answer=0
    dic={"A":0,"E":1,"I":2,"O":3,"U":4}
    part_sum=[781,156,31,6,1]
    for x in range(len(word)):
        answer+=(dic[word[x]])*part_sum[x]
    answer+=len(word)
    return answer