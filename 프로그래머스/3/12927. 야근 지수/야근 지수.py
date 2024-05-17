from heapq import *
def solution(n, works):
    works=list(map(lambda x: -x,works))
    heapify(works)
    while n and works:
        x=heappop(works)
        if x+1!=0:
            heappush(works,x+1)
        n-=1
    answer=sum(map(lambda x: x**2,works))
    return answer