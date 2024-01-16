#신발끈 공식
import sys
input=sys.stdin.readline
N=int(input())
coords=[]
for _ in range(N):
    coords.append(list(map(int,input().split())))
answer=0
for i in range(N-1):
    answer+=coords[i][0]*coords[i+1][1]
    answer-=coords[i+1][0]*coords[i][1]
answer+=coords[N-1][0]*coords[0][1]
answer-=coords[0][0]*coords[N-1][1]
print(abs(round(answer/2,2)))