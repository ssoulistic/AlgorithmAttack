def solution(n, s):
    answer=[s//n for _ in range(n)]
    for i in range(1,s%n+1):
        answer[-i]+=1
    if 0 in answer:
        answer=[-1]
    return answer