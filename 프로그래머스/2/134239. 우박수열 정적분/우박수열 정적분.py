def solution(k, ranges):
    # 1. 짝수 =>나누기 2
    # 2. 홀수 => 3 곱하고 1더하고
    # 3. 1보다 크면 반복.
    
    S=[0]
    count=0
    before=k
    while k!=1:
        if k % 2 ==0:
            k/=2
        else:
            k=3*k+1
        count+=1
        
        S.append(S[-1]+(before+k)/2)
        before=k
    result=[]
    for s,e in ranges:
        if s>len(S)-1+e:
            result.append(-1)
        else:
            result.append(S[e-1]-S[s])
    return result