N,M=map(int,input().split())
temp=[]
answer=[]
given=sorted(map(int,input().split()))
def select_num():
    #n이 0이거나 m이 0 시 종료
    if len(temp)==M:
        if sorted(temp) not in answer:
            answer.append(temp.copy())
            print(*temp.copy())
    for i in given:
        if i not in temp:
            temp.append(i)
            select_num()
            temp.pop()
select_num()
