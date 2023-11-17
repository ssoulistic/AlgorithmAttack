N,M=map(int,input().split())
temp=[]
answer=[]
given=sorted(map(int,input().split()))

def select_num():
    if len(temp)==M:
        answer.append(temp.copy())
        print(*temp.copy())
        return
    for i in given:
        temp.append(i)
        select_num()
        temp.pop()
select_num()