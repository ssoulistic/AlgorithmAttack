def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x : [x[col-1],-x[0]])
    S_i=[]
    for row in range(row_begin,row_end+1):
        S_i.append(sum(map(lambda y: y % row ,data[row-1])))
    answer=0
    for i in S_i:
        answer=answer^i
    return answer