def solution(today, terms, privacies):
    dic={}
    answer = []
    for t in terms:
        choose,term=t.split()
        dic[choose]=int(term)
    
    y2,m2,d2=map(int,today.split("."))
    
    for idx,p in enumerate(privacies):
        date,choose=p.split()
        year,month,day=map(int,date.split("."))
        if month+dic[choose]>12: # 24개월이면.. 1년 더하고 12월.
            year+=(month+dic[choose]-1)//12
            month=(month+dic[choose]-1)%12+1
        else:
            month+=dic[choose]
            
        if y2>year or (y2==year and m2>month) or (y2==year and m2 ==month and d2>=day):
            answer.append(idx+1)
    return answer