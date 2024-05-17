import sys
input=sys.stdin.readline
N=int(input())
seq=[]
for _ in range(N):
    a,b=map(int,input().split())
    seq.append([a,b])
seq.sort()
longest=[]
idx_long=[0 for _ in range(N)]
def binsearch(start,end,k):
    if start>=end:
        return end
    mid=(start+end)//2
    if longest[mid]<k:
        return binsearch(mid+1,end,k)
    elif longest[mid]>=k:
        return binsearch(start,mid,k)

    
for i in range(N):
    if longest:
        if longest[-1]<seq[i][1]:
            longest.append(seq[i][1])
            idx_long[i]=len(longest)-1
        else:
            x=binsearch(0,len(longest)-1,seq[i][1])
            longest[x]=seq[i][1]
            idx_long[i]=x
    else:
        longest.append(seq[i][1])
        idx_long[i]=len(longest)-1


t=len(longest)
idx=len(idx_long)-1
answer=[]
while t:
    if idx_long[idx]==t-1:
        t-=1
    else:
        answer.append(seq[idx][0])
    idx-=1
while idx>-1:
    answer.append(seq[idx][0])
    idx-=1

print(N-len(longest))
answer=answer[::-1]
for f in range(N-len(longest)):
    print(answer[f])