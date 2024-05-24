from heapq import heappop, heappush

def solution(jobs):
    n = len(jobs)
    jobs.sort()  # jobs를 시작 시간 기준으로 정렬
    answer = 0
    now = 0
    queue = []
    i = 0  # jobs 리스트의 인덱스

    while i < n or queue:
        # 현재 시간보다 일찍 도착한 작업을 모두 큐에 추가
        while i < n and jobs[i][0] <= now:
            heappush(queue, (jobs[i][1], jobs[i][0]))
            i += 1
        
        if queue:
            t, s = heappop(queue)
            now += t
            answer += now - s
        else:
            # 큐가 비어 있으면 다음 작업의 시작 시간으로 이동
            if i < n:
                now = jobs[i][0]

    return answer // n
