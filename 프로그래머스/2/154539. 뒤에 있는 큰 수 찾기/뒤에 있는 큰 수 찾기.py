def solution(numbers):
    B=list()
    answer=list(-1 for _ in range(len(numbers)))
    for i in range(len(numbers)-1):
        B.append((numbers[i],i))
        while B and B[-1][0]<numbers[i+1]:
            answer[B.pop()[1]]=numbers[i+1]
    return answer