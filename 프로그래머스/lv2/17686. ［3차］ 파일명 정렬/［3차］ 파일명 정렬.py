import re
def solution(files):
    sur=[]
    answer = []
    for file_name in files:
        num_start,num_end=(re.search('[0-9]+',file_name).span())
        head,number,tail=file_name[:num_start],file_name[num_start:num_end],file_name[num_end:]
        sur.append([head,number,tail])

    sur.sort(key=lambda x : (x[0].lower(),int(x[1])))

    for s in sur:
        answer.append(s[0]+str(s[1])+s[2])
    return answer
        
