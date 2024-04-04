# 당연히 bfs라고 생각하고 풀었는데 시간초과가 나서 Pypy3로 제출해서 통과했었다.
# 그런데 치킨거리는 그냥 좌표 차이로 구할 수 있어서 그걸 비교하면 됐었던것...이었다..
# 익숙한 문제도 다시 찬찬히 생각해볼 필요가 있을듯 하다.
import sys
input=sys.stdin.readline
from itertools import combinations
N,M=map(int,input().split())
city=[]
chicken=[]
home=[]
for r in range(N):
    line=list(map(int,input().split()))
    for c in range(N):
        if line[c]==2:
            chicken.append([r,c])
        elif line[c]==1:
            home.append([r,c])
    city.append(line)

answer=N**N
for combo in combinations(chicken,M):
    chicken_distance=0
    for hr,hc in home:
        home_min=N**N
        for rr,cc in combo:
            if home_min>abs(rr-hr)+abs(cc-hc):
                home_min=abs(rr-hr)+abs(cc-hc)
        chicken_distance+=home_min
    if answer>chicken_distance:
        answer=chicken_distance
print(answer)
    
