def solution(queue1, queue2):
    if (sum(queue1)+sum(queue2)) % 2 ==1:
        return -1
    merge=(queue1+queue2)
    target=(sum(queue1)+sum(queue2))//2
    count=0
    Q1,Q2=sum(queue1),sum(queue2)
    i1,i2=0,len(queue1)
    
    while Q1!=target and Q1>0 and Q2>0 and count<=len(queue1)*4:
        if Q1>Q2:
            Q1-=merge[i1]
            Q2+=merge[i1]
            i1+=1
        elif Q1<Q2:
            Q1+=merge[i2]
            Q2-=merge[i2]
            i2+=1
        i1%=len(merge)
        i2%=len(merge)
        count+=1
        
    if Q1!=target:
        answer=-1
    else:
        answer=count
        
    return answer