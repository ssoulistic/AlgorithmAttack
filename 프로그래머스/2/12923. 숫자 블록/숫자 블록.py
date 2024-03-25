def solution(begin, end):
    dv={}
    def divider(num):
        if dv.get(num):
            return dv[num]
        
        if num==1:
            return 0
        elif num==2:
            return 1
        dv[num]=1
        for i in range(2,int(num**0.5)+1):
            if num % i==0:
                dv[num]=i
                if 1<num//i<=10000000:
                    dv[num]=num//i
                    return num//i
        
        return dv[num]
            
    # 자기자신을 제외한 최대 약수.
    answer=[]
    for j in range(begin,end+1):
        answer.append(divider(j))
    return answer