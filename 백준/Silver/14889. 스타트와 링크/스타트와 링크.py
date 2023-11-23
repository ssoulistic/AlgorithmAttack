N=int(input())
stats=[]
link=[0 for _ in range(N)]
mini=200*10
for _ in range(N):
    stats.append(list(map(int,input().split())))

def team(idx,depth):
    global mini
    if depth==N//2:
        result=0
        for l in range(N):
            for k in range(l+1,N):
                if l!=k:
                    if link[l] and link[k]:
                        result+=(stats[l][k]+stats[k][l])
                    elif link[l]==0 and link[k]==0:
                        result-=(stats[l][k]+stats[k][l])
        if mini>abs(result):
            mini=abs(result)
        return
    for i in range(idx,N):
        if not link[i]:
            link[i]+=1
            team(i,depth+1)
            link[i]-=1
team(0,0)
print(mini)