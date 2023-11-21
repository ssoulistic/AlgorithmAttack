N,M,B=map(int,input().split())
ground={}
answer=[]
for _ in range(N):
    for g in map(int,input().split()):
        if ground.get(g):
            ground[g]+=1
        else:
            ground[g]=1
start=min(ground.keys())
end=max(ground.keys())

for floor in range(start,end+1):
    time=0
    blocks=0
    for k,v in ground.items():
        if k>=floor: #블럭을 제거해야함.
            time+=2*(k-floor)*v
            blocks-=(k-floor)*v
        else: # 쌓아 올려야함.
            time+=(floor-k)*v
            blocks+=(floor-k)*v
    if B-blocks>=0:
        if answer:
            if answer[0]>time:
                answer=(time,floor)
            elif answer[0]==time:
                if answer[1]<floor:
                    answer=(time,floor)
        else:
            answer=(time,floor)
print(*answer)
