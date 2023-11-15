#24060 병합정렬 - 재귀
import sys
answer=[]
def merge_sort(Li_A,start,end):
    if start<end:
        mid=(start+end)//2
        merge_sort(Li_A,start,mid) # 좌측 정렬
        merge_sort(Li_A,mid+1,end) # 우측 정렬
        answer.extend(merge(Li_A,start,mid,end)) # 마지막 병합 정렬
def merge(Li_B,start,mid,end): # 두개의 리스트 비교하여 정렬하기.
    i=start
    j=mid+1
    t=0
    temp=[]

    while i<=mid and j<=end: #좌 우 리스트 한개씩..
        if Li_B[i]<=Li_B[j]:
            temp.append(Li_B[i])
            i+=1
        else:
            temp.append(Li_B[j])
            j+=1
        t+=1

    while i<=mid:
        temp.append(Li_B[i])
        i+=1
    
    while j<=end:
        temp.append(Li_B[j])
        j+=1
    
    i=start
    t=0
    while i<=end:
        Li_B[i]=temp[t]
        t+=1
        i+=1
    
    return temp
N,K=map(int,sys.stdin.readline().split())
A=list(map(int,sys.stdin.readline().split()))

merge_sort(A,0,len(A)-1)
if K>len(answer):
    print(-1)
else:
    print(answer[K-1])
