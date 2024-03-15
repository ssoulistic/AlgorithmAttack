A,B,C,D,E=map(int,input().split())
M=5
load=[1]*A+[2]*B+[3]*C+[4]*D+[5]*E
truck=[]

load.sort()
while load:
    next=load.pop()
    loaded=False
    for i in range(len(truck)):
        if truck[i]+next<=M:
            truck[i]+=next
            loaded=True
            break
    if not loaded:
        truck.append(next)
print(len(truck))