from heapq import *
def solution(jobs):
    n=len(jobs)
    heapify(jobs)
    answer = 0
    now=0
    queue=[]
    while jobs or queue:
        while jobs and jobs[0][0]<=now:
            start,time=heappop(jobs)
            heappush(queue,[time,start])
        if queue:
            t,s=heappop(queue)
            now+=t
            answer+=now-s
        elif jobs[0][0]>now:
            now=jobs[0][0]
    return answer//n