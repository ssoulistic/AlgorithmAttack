import sys
input=sys.stdin.readline
N,M=map(int,input().split())
seq=sorted(map(int,input().split()))
counter={}
for s in seq:
    if counter.get(s):
        counter[s]+=1
    else:
        counter[s]=1
#차례로..set 이용해보기.
answer=set()
pack=[]
def backt():
    if len(pack)==M:
        answer.add(tuple(pack))
        return
    for num in seq:
        if counter[num]>0:
            pack.append(num)
            counter[num]-=1
            backt()
            pack.pop()
            counter[num]+=1
    return
backt()
for ans in sorted(answer):
    print(*ans)
