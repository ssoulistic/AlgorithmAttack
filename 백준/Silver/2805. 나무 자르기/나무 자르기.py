N,M=map(int,input().split())
trees=list(map(int,input().split()))

def cutting(height):
    part=0
    for i in trees:
        if i>height:
            part+=i-height
    return part

def binsearch(start,end):
    while start<=end:
        mid=(start+end)//2
        if cutting(end)>=M: 
            return end
        elif cutting(mid+1)>=M:
            start=mid+1
        elif cutting(start)>=M:
            end=mid
print(binsearch(0,max(trees)))