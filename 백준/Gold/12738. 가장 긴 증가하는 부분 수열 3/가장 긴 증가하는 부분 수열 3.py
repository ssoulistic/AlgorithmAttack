import sys
input=sys.stdin.readline
N=int(input())
A=list(map(int,input().split()))
longest=[]
for i in range(N):
    if longest:
        if longest[-1]<A[i]:
            longest.append(A[i])
        else:
            s=0
            e=len(longest)
            while s<e:
                mid=(s+e)//2
                if longest[mid]<A[i]:
                    s=mid+1
                else:
                    e=mid
            longest[e]=A[i]
    else:
        longest.append(A[i])
print(len(longest))
