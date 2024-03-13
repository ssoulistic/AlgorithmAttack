def solution(n, t, m, p):
    # n진법 미리 구할 개수 t 게임 인원 m 튜브 순서 p
    zinbub={}
    for k in range(16):
        zinbub[k]=hex(k)[2:].upper()
    
    def convert(z,num):        
        result=""
        while num:
            num,r=divmod(num,z)
            result=str(zinbub[r])+result
        return result
    
    answer='0'
    i=1
    while len(answer)<t*m:
        answer+=convert(n,i)
        i+=1        
    return answer[p-1::m][:t]