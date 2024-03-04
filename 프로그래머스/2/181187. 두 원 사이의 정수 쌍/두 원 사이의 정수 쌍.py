def solution(r1, r2):
    answer=0
    # r2 내부 경계o
    # r1 내부 경계x
    for i in range(1,r2):
        answer+=int((r2**2-i**2)**0.5)
    for i in range(1,r1):
        if int((r1**2-i**2)**0.5)==(r1**2-i**2)**0.5:
            answer+=1
        answer-=int((r1**2-i**2)**0.5)
    answer+=r2-r1+1
    return answer*4