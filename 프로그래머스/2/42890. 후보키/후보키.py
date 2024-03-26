from itertools import combinations
def solution(relation):
    pool=[]
    for i in range(1,len(relation)+1):
        for combi in combinations([j for j in range(len(relation[0]))],i):
            Flag=False
            for p in pool:
                if all(True if pp in combi else False for pp in p):
                    Flag=True
            if Flag==True:
                continue
            temp=[]
            for k in range(len(relation)):              
                st=""
                for c in combi:
                    st+=relation[k][c]
                temp.append(st)
            if len(temp)==len(set(temp)):
                pool.append(combi)
    return len(pool)