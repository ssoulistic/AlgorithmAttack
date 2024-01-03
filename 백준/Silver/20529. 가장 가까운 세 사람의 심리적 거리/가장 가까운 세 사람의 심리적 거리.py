import sys
T=int(sys.stdin.readline())

def distance(a,b):
    dis=0
    for i in range(4):
        if a[i]!=b[i]:
            dis+=1
    return dis

def three():
    global candi
    global answer
    if len(candi)==3:
        x1,x2,x3=mbti[candi[0]],mbti[candi[1]],mbti[candi[2]]
        p=distance(x1,x2)+distance(x2,x3)+distance(x1,x3)
        if answer>p:
            answer=p
        return
    for m in range(len(mbti)):
        if m not in candi:
            candi.append(m)
            three()
            candi.pop()
    return


for _ in range(T):
    N=int(sys.stdin.readline())
    mbti=sys.stdin.readline().split()
    answer=16
    candi=[]

    # 비둘기집의 원리
    if N>=48:
        answer=0
    else:
        three()
    print(answer)