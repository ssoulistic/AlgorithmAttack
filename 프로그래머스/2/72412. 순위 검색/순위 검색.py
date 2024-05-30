def bs(score_list,target):
    start=0
    end=len(score_list)
    while start<end:
        mid=(start+end)//2
        if score_list[mid]>=target:
            end=mid
        else:
            start=mid+1
    return end
    

def solution(info, query):
    dic={}
    answer = []
    for c1 in ["-","python","java","cpp"]:
        for c2 in ["-","backend","frontend"]:
            for c3 in ["-","junior","senior"]:
                for c4 in ["-","chicken","pizza"]:
                    dic[(c1,c2,c3,c4)]=[]
    for person in info:
        language,position,career,soul_food,score=person.split()
        for a1 in ["-",language]:
            for a2 in ["-",position]:
                for a3 in ["-",career]:
                    for a4 in ["-",soul_food]:
                        dic[(a1,a2,a3,a4)].append(int(score))
    
    for score_list in dic.values():
        score_list.sort()
    
    for q in query:
        language,position,career,remain=q.split(" and ")
        soul_food,score=remain.split()
        
        pass_min=bs(dic[(language,position,career,soul_food)],int(score))
        answer.append(len(dic[(language,position,career,soul_food)])-pass_min)
    return answer