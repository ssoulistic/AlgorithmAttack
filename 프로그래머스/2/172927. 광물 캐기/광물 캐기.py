def solution(picks, minerals):
    # 자원 수치화
    for m in range(len(minerals)):
        if minerals[m]=="diamond":
            minerals[m]=25
        elif minerals[m]=="iron":
            minerals[m]=5
        elif minerals[m]=="stone":
            minerals[m]=1
    # 자원 정렬
    pick_count=len(minerals)//5
    seq=[]
    for i in range(pick_count):
        seq.append(minerals[5*i:5*i+5])
    seq.append(minerals[5*(pick_count):])
    
    
    if 5*sum(picks)<len(minerals):
        seq=seq[:sum(picks)]
        
    seq.sort(key=lambda x: sum(x))
    
    # 곡괭이 순서대로 
    picks=[25]*picks[0]+[5]*picks[1]+[1]*picks[2]
    picks.sort()
    
    tired=0
    while picks and seq:
        m=seq.pop()
        p=picks.pop()
        tired+=sum(map(lambda x: x//p if x//p else 1,m))
    return tired