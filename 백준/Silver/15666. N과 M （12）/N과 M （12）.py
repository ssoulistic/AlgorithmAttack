N,M=map(int,input().split())
seq=list(map(int,input().split()))
check=set()
for s in seq:
    check.add(s)
check=sorted(check)
temp=[]
answer=set()
def backt():
    if len(temp)==M:
        answer.add(tuple(temp.copy()))
        return
    for c in check:
        if temp and temp[-1]>c:
            continue
        temp.append(c)
        backt()
        temp.pop()
backt()
for ans in sorted(answer):
    print(*ans)

    