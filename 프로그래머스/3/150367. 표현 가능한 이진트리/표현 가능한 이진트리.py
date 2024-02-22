def solution(numbers):
    import sys
    sys.setrecursionlimit(10**9)
    answer=[]
    def check(sub):
        mid=len(sub)//2
        # root가 1인경우 => 양쪽 가능
        # root가 0인경우 => 모두 0이여야함.
        if len(sub)>=3:
            if sub[mid]=="1":
                if check(sub[:mid]) and check(sub[mid+1:]):
                    return True
                else:
                    return False
            else:
                if "1" in sub:
                    return False
                else:
                    return True
        else:
            return True
                    
    
    for i in numbers:
        temp=str(bin(i)[2:])
        
        l=len(temp)
        # l의 길이가 2**n-1 인지 (0을 붙였을떄, 안붙였을때)
        count=0
        while (l+1+count)&(l+count)!=0:
            count+=1
        temp="0"*count+temp
        if check(temp):
            answer.append(1)
        else:
            answer.append(0)
            
    
    return answer