from collections import deque
import sys
input=sys.stdin.readline 

T=int(input())
def dfs(cur):
    current_list=deque()
    while True:
        if visited[cur]:
            if cur in current_list:
                return len(current_list)-current_list.index(cur)
            return 0
        current_list.append(cur)
        visited[cur]=True
        cur=sel[cur]

for _ in range(T):
    n=int(input())
    answer=n
    sel=[0]
    sel.extend(list(map(int,input().split())))
    visited=[False for _ in range(n+1)]
    for k in range(1,n+1):
        answer-=dfs(k)
    print(answer)