from itertools import product
def solution(users, emoticons):
    n=len(emoticons)
    permute=product([l for l in range(1,5)],repeat=n)
    result=[0,0]
    for p in permute:
        acc=0
        sub=0
        for sale,limit in users:
            temp=0
            for i in range(n):
                if p[i]*10>=sale:
                    temp+=(emoticons[i]*(100-p[i]*10)/100)
            if temp>=limit:
                sub+=1
                temp=0
            acc+=temp
        if sub>result[0]:
            result=[sub,acc]
        elif sub==result[0]:
            if acc>result[1]:
                result[1]=acc
                
    return result