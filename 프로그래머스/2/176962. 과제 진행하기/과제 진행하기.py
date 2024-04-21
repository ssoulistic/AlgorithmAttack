from collections import deque
def solution(plans):
    answer=[]
    # 숙제를 시작 => 시간이 되면 그 숙제를 시작. => 미룬건 가장 마지막에 멈춘것 부터
    # 1. 미뤄둔숙제들 => stack
    # 2. 숙제 시작 => 그 다음 숙제 시작 시간 vs 현재 숙제 남은 시간 + 미뤄둔 숙제 
    # 숙제 우선 순위 // 새로운 숙제 > 진행중 숙제 > 미뤄둔 숙제
    plans.sort(key=lambda x: x[1])
    plans=deque(plans)
    pending=[]
    now_hw=["",0,0] #과목,시작시간, 남은 시간
    while plans:
        # 1. 시간이 되면 하던 숙제 미루고 숙제 시작
        next_hw=plans.popleft()
        subject,time,left=next_hw
        h,m=map(int,time.split(":"))
        left=int(left)
        time=60*h+m
        if now_hw[1]+now_hw[2]>time:
            pending.append([now_hw[0],now_hw[1]+now_hw[2]-time])
        else:
            # 여유 타임
            if now_hw[0]!="":
                answer.append(now_hw[0])
            bonus=time-(now_hw[1]+now_hw[2])
            while pending and bonus:
                sub2,time2=pending.pop()
                if bonus<time2:
                    time2-=bonus
                    bonus=0
                    pending.append([sub2,time2])
                else:
                    bonus-=time2
                    answer.append(sub2)
        now_hw=[subject,time,left]
    answer.append(subject)
    while pending:
        answer.append(pending.pop()[0])
    return answer