import sys
input=sys.stdin.readline
N=int(input())
M=int(input())
city=[]
group=[i for i in range(N)]
for _ in range(N):
    city.append(list(map(int,input().split())))
visit=list(map(int,input().split()))

# 1. 그룹화
# 2. visit에 나온 도시들의 부모가 모두 같으면 YES 아니면 NO

def find(num):
    if num!=group[num]:
        group[num]=find(group[num])
    return group[num]

def union(a,b):
    a=find(a)
    b=find(b)
    if a>b:
        group[a]=b
    else:
        group[b]=a

for row in range(N):
    for col in range(N):
        if city[row][col]==1:
            union(row,col)
            
answer=set()
for v in visit:
    answer.add(group[v-1])
if len(answer)==1:
    print("YES")
else:
    print("NO")