def solution(number,k):
    i=0
    while i<len(number)-1 and k>0:
        if int(number[i])<int(number[i+1]):
            number=number.replace(number[i],"",1)
            k-=1
            if i>=1:
                i-=1
        else:
            i+=1
    if k!=0:
        return number[:-k]
    else:
        return number