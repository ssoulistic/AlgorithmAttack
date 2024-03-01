def solution(s):
    length=len(s)//2+1
    # 끊는 길이.
    mini=len(s)
    for long in range(1,length):
        answer = 0
        before=["",0]
        for idx in range(0,len(s),long):
            if before[0]!=s[idx:idx+long]:
                answer+=len(before[0])
                if before[1]:
                    answer+=len(str(before[1]+1))
                before[0]=s[idx:idx+long]
                before[1]=0
            else:
                before[1]+=1
        answer+=len(before[0])
        if before[1]:
            answer+=len(str(before[1]+1))
        if mini>answer:
            mini=answer
    return mini