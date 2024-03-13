def solution(msg):
    dic={}
    for i in range(26):
        dic[chr(ord("A")+i)]=i+1
    s,e=0,1
    answer = []
    
    while e<=len(msg):
        if (dic.get(msg[s:e-1]) and not dic.get(msg[s:e])):
            answer.append(dic[msg[s:e-1]])
            dic[msg[s:e]]=len(dic)+1
            s=e-1
        e+=1
    answer.append(dic[msg[s:e]])
    return answer