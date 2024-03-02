import sys
input=sys.stdin.readline
N=int(input())
k=int(input())
start=1
end=k
answer=0

while start<=end:
    mid=(start+end)//2
    count=0
    
    for i in range(N):
        count+=min(mid//(i+1),N)
        
    if k<=count:
        answer=mid
        end=mid-1
    elif k>count:
        start=mid+1
print(answer)