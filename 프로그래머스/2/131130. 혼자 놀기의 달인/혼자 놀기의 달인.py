def solution(cards):
    opened=[False for _ in range(len(cards))]
    
    def box(n):
        if opened[n-1]:
            return False
        opened[n-1]=True
        que=[]
        que.append(n-1)
        count=1
        while que:
            next=que.pop(0)
            if not opened[cards[next]-1]:
                opened[cards[next]-1]=True
                que.append(cards[next]-1)
                count+=1
                
        return count
    
    answer=[]
    for i in range(1,len(cards)+1):
        check=box(i)
        if check!=False:
            answer.append(check)
    answer.sort(reverse=True)
    if len(answer)<=1:
        return 0
    else:
        return answer[0]*answer[1]