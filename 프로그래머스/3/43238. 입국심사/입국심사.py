def solution(n, times):
    start=1
    end=1e15
    while start<end:
        mid=(start+end)//2
        person=0
        for t in times:
            person+=mid//t
        if  person<n:
            start=mid+1
        elif person>=n:
            end=mid
    return end