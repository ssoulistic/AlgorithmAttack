def solution(arrayA, arrayB):
    def gcd(a,b):
        while a % b:
            b,a=a%b,b
        return b
    # 각각의 최대공약수 => 상대는 모두 안나눠지는 조건.
    gcdA=arrayA[0]
    for i in range(1,len(arrayA)):
        if gcdA>arrayA[i]:
            gcdA=gcd(gcdA,arrayA[i])
        else:
            gcdA=gcd(arrayA[i],gcdA)
    
    gcdB=arrayB[0]
    for i in range(1,len(arrayB)):
        if gcdB>arrayB[i]:
            gcdB=gcd(gcdB,arrayB[i])
        else:
            gcdB=gcd(arrayB[i],gcdB)
    for j in range(len(arrayB)):
        if arrayB[j] % gcdA ==0:
            gcdA=0
            break
    for j in range(len(arrayA)):
        if arrayA[j] % gcdB ==0:
            gcdB=0
            break
    answer=max(gcdA,gcdB)        
    return answer