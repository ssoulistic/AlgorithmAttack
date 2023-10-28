T=int(input())
mem=[0 for _ in range(T+2)]
for _ in range(T):
    next=list(map(int,input().split()))
    temp=[]
    for i in range(len(next)):
        temp.append(max(mem[i],mem[i+1])+next[i])
    for j in range(len(temp)):
        mem[j+1]=temp[j]
print(max(mem))
    