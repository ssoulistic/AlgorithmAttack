def solution(food_times, k):
    maximum=max(food_times)
    def binsearch(start,end, es, ee):
        mid=(start+end)//2
        em = eat(mid)
        emp1 = eat(mid+1)
        if start>=end:
            return end
        if es>k:
            return start
        elif em>k:
            return binsearch(start,mid,es,em)
        elif ee>k:
            return binsearch(mid+1,end,emp1,ee)
        elif ee==k:
            return end
        
    # 한바퀴 돌면서 자신보다 작은 값들을 더하는 함수
    def eat(n):
        result=0
        for i in food_times:
            if i<n:
                result+=i
            else:
                result+=n
        return result
    
    # 한바퀴 돌면서 자신보다 크거나 같은 수들을 카운팅하는 함수.
    def search(n,target):
        result=0
        for i in range(len(food_times)):
            if food_times[i]>=n:
                result+=1
            if result==target:
                return i+1
        return search(n+1,target)
    
    if eat(maximum)<k+1:
        answer=-1
    else:
        target_line=binsearch(1,maximum,eat(1),eat(maximum)) # k가있는곳.
        answer=search(target_line,k+1-eat(target_line-1))
    return answer
