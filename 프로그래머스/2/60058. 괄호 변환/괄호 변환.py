def bal(p):
    if p.count("(")==p.count(")"):
        return True
    else:
        return False

def correct(p):
    close=[]
    for i in range(len(p)):
        if p[i]==")" and close and close[-1]=="(":
            close.pop()
        else:
            close.append(p[i])
    if close:
        return False
    else:
        return True

def solution(p):
    if p=="":
        return p
    answer=""
    i=1
    while not bal(p[:i]):
        i+=1
        
    u,v=p[:i],p[i:]
    if correct(u):
        return u+solution(v)
    else:
        answer+="("+solution(v)+")"
        if len(u)>2:
            u=u[1:-1]
            temp=""
            for s in u:
                if s=="(":
                    temp+=")"
                else:
                    temp+="("
            answer+=temp
    return answer