import heapq
def solution(book_time):
    # 정렬문제 - 시작시간을 기준으로 스택.
    # 4칸짜리로 정렬. 스택에는 마지막 시간+10 만 표시.
    # 마지막 시간
    # heap 원소의 갯수=> 최소값
    bque=[]
    best=[-1]
    heapq.heapify(best)
    for start,end in book_time:
        sh,sm=map(int,start.split(":"))
        eh,em=map(int,end.split(":"))
        bque.append([sh*60+sm,eh*60+em+10])
    for st,et in sorted(bque):
        if best[0]<=st: # 가장 빠른 시간이 종료시간보다 빠르면.
            heapq.heappop(best)
            heapq.heappush(best,et)
        else:
            heapq.heappush(best,et)    
    return len(best)