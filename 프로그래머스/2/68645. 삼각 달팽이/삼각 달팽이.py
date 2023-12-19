def solution(n):
    answer = [0 for _ in range(n*(n+1)//2)]
    height,seq=n,0
    mode=0 #방향.
    acc=0
    for i in range(n,-1,-1):
        for j in range(acc+1,acc+i+1):
            if mode%3 ==0: #좌하
                height-=1
            elif mode%3==1:
                seq+=1
            elif mode%3 ==2:
                height+=1
                seq-=1
            answer[(height-n)*(height-n+1)//2+seq]=j
        mode+=1
        acc+=i
    return answer