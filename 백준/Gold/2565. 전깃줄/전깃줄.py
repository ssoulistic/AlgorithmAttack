T=int(input())
elecline=[]
LIS=[1 for _ in range(T)]
for _ in range(T):
    elecline.append(list(map(int,input().split())))
elecline.sort()

for i in range(T):
    for j in range(i+1,T):
        if elecline[i][1]<elecline[j][1]:
            LIS[j]=max(LIS[j],LIS[i]+1)

print(T-max(LIS))