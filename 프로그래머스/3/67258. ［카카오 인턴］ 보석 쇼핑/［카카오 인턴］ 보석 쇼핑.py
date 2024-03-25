def solution(gems):
    global result
    total=len(set(gems))
    result=[1,len(gems)]
    
    def check(min_x,max_x):
        global result
        length_x=max_x-min_x
        length_r=result[-1]-result[0]
        # 1. 길이가 짧은지.
        if length_x<length_r:
            result=[min_x+1,max_x+1]
        # 2. 길이가 같다면 앞인지.
        elif length_x==length_r:
            if min_x+1<result[0]:
                result=[min_x+1,max_x+1]
        return

    dic={}
    s,e=0,0
    while s<=e and e<len(gems):
        dic[gems[e]]=e
        if len(dic)<total:
            e+=1
        elif len(dic)==total:
            if e-s<result[-1]-result[0]:
                check(s,e)
            if dic[gems[s]]==s:
                del dic[gems[s]]
            s+=1
    
    return result
