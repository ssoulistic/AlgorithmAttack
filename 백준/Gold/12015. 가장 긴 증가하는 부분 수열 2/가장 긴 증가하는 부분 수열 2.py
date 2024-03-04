import sys
input=sys.stdin.readline
N=int(input())
seq=list(map(int,input().split()))
mem=[0]

def binsearch(start,end,num):
    mid=(start+end)//2
    if start>=end:
        return end
     
    if mem[end]<num:
        return end
    elif mem[mid]<num:
        return binsearch(mid+1,end,num)
    else:
        return binsearch(start,mid,num)
    
for i in seq:
    if mem[-1]<i:
        mem.append(i)
    else:
        mem[binsearch(0,len(mem)-1,i)]=i
print(len(mem)-1)