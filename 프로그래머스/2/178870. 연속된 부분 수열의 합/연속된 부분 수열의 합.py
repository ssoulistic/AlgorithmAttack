def solution(sequence, k):
    answer=[0,len(sequence)]
    psum=0
    e=0
    for s in range(len(sequence)):
        while psum<k and e<len(sequence):
            psum+=sequence[e]
            e+=1
        if psum==k:
            if answer[1]-answer[0]>e-s-1:
                answer=[s,e-1]
            elif answer[1]-answer[0]==e-s-1 and answer[0]>s:
                answer=[s,e-1]
        psum-=sequence[s]
            
    return answer