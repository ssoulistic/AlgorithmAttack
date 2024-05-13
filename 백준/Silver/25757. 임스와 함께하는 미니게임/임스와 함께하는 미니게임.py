import sys
input=sys.stdin.readline
N,game=input().split()
N=int(N)
played={}
party=0
need=0
if game=="Y":
    need=1
elif game=="F":
    need=2
elif game=="O":
    need=3

answer=0
for _ in range(N):
    player=input().strip()
    if played.get(player)==None:
        played[player]=True
        party+=1
        if party==need:
            answer+=1
            party=0
        
print(answer)

    