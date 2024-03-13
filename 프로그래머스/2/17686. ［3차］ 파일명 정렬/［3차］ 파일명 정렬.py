def solution(files):
    result = []
    for file_name in files:
        i=0
        HEAD,NUMBER,TAIL="","",""
        while i<len(file_name) and not file_name[i].isdigit():
            HEAD+=file_name[i]
            i+=1
        while i<len(file_name) and file_name[i].isdigit():
            NUMBER+=file_name[i]
            i+=1
        TAIL=file_name[i:]
        result.append([HEAD,int(NUMBER),NUMBER,TAIL])
    result.sort(key=lambda x: [x[0].lower(),x[1]])
    answer=[]
    for a1,a2,a3,a4 in result:
        answer.append(a1+a3+a4)        
    return answer