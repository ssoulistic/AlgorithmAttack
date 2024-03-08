def solution(record):
    answer=[]
    log = []
    user={}
    for msg in record:
        rec=msg.split()
        if rec[0]=="Leave":
            log.append([rec[1],"님이 나갔습니다."])
        elif rec[0]=="Enter":
            user[rec[1]]=rec[2]
            log.append([rec[1],"님이 들어왔습니다."])
        elif rec[0]=="Change":
            user[rec[1]]=rec[2]
    for uid,msg in log:
        answer.append(user[uid]+msg)
    return answer