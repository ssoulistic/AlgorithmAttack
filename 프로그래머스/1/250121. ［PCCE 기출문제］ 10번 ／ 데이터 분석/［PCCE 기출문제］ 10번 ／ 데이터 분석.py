def solution(data, ext, val_ext, sort_by):
    answer=[]
    dic={"code":0,"date":1,"maximum":2,"remain":3}
    crit=dic[ext]
    for sample in data:
        if sample[crit]<val_ext:
            answer.append(sample)   
    answer.sort(key=lambda x : x[dic[sort_by]])
    return answer