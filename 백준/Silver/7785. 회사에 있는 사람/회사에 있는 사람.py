import sys
n=int(sys.stdin.readline())
room={}
answer=[]
for _ in range(n):
    name,stat=sys.stdin.readline().split()
    room[name]=stat
for k,v in room.items():
    if v=="enter":
        answer.append(k)
answer.sort(reverse=True)
for i in range(len(answer)):
    print(answer[i])