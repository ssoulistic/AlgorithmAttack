import sys
input=sys.stdin.readline
T=int(input())

def dfs(cur):
    while True:
        if visited[cur]:
            Flag=False
            for l in range(len(current_list)):
                if Flag:
                    teamed[current_list[l]]=True
                elif current_list[l]==cur:
                    Flag=True
                    teamed[current_list[l]]=True
            return
        current_list.append(cur)
        visited[cur]=True
        cur=sel[cur]


for _ in range(T):
    n=int(input())
    students=list(map(int,input().split()))
    sel=[0 for _ in range(n+1)]
    for j in range(n):
        sel[j+1]=students[j]
    visited=[False for _ in range(n+1)]
    teamed=[False for _ in range(n+1)]
    for k in range(1,n+1):
        current_list=list()
        dfs(k)
    print(n-teamed.count(True))