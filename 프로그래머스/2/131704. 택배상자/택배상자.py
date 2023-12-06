def solution(order):
    sub=[]
    answer=0
    for i in range(1,len(order)+1):
        if i ==order[answer]:
            answer+=1
        else:
            sub.append(i)
        while sub and sub[-1]==order[answer]:
            sub.pop()
            answer+=1
        
    return answer