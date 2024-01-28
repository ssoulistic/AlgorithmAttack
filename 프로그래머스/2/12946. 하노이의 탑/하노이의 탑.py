def solution(n):
    answer = []
    def hanoi(num,start,end):
        if num==1:
            answer.append([start,end])
            return 
        dest=6-start-end
        hanoi(num-1,start,dest)
        answer.append([start,end])
        hanoi(num-1,dest,end)
    hanoi(n,1,3)
    return answer