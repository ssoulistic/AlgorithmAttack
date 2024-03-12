def solution(food_times, k):
    maximum=max(food_times)
    def binsearch(start,end):
        while start<end:
            mid=(start+end)//2
            if eat(start)>k:
                return start
            elif eat(mid)>k:
                end=mid
            elif eat(end)>=k:
                start=mid+1
        return end
    eaten={}
    # 한바퀴 돌면서 자신보다 작은 값들을 더하는 함수
    def eat(n):
        if eaten.get(n):
            return eaten[n]
        result=0
        for i in food_times:
            if i<n:
                result+=i
            else:
                result+=n
        eaten[n]=result
        return eaten[n]
    
    # 한바퀴 돌면서 자신보다 크거나 같은 수들을 카운팅하는 함수.
    def search(n,target):
        result=0
        for i in range(len(food_times)):
            if food_times[i]>=n:
                result+=1
            if result==target:
                return i+1
    
    if eat(maximum)<k+1:
        return -1
    else:
        target_line=binsearch(0,maximum) # k가있는곳.
        if eat(target_line)<k+1:
            return search(target_line+1,k+1-eat(target_line-1))
        else:
            return search(target_line,k+1-eat(target_line-1))
    