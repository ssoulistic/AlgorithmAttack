import sys
input=sys.stdin.readline 

T=int(input())

def dfs(cur):
    while True:
        if visited[cur]:
            for l in range(len(current_list)):
                if current_list[l]==cur:
                    return len(current_list)-l
            return 0
        current_list.append(cur)
        visited[cur]=True
        cur=sel[cur]


for _ in range(T):
    n=int(input())
    answer=n
    students=list(map(int,input().split()))
    sel=[0 for _ in range(n+1)]
    for j in range(n):
        sel[j+1]=students[j]
    visited=[False for _ in range(n+1)]
    teamed=[False for _ in range(n+1)]
    for k in range(1,n+1):
        current_list=list()
        answer-=dfs(k)
    print(answer)