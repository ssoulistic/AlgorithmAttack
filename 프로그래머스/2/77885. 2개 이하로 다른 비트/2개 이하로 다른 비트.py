def solution(numbers):
    # 비트 0의 자리가 0이면 +1
    # 비트 0의 자리가 1이면 비트 1의자리  10101 11011 -> 가장 작은 곳에 위치한 0 과 1 바꿔주기.
    answer = []
    for number in numbers:
        x=list(bin(number)[2:])
        if x[-1]=="0":
            answer.append(int("".join(x),2)+1)
        else:
            Flag=0
            for i in range(len(x)-1,-1,-1):
                if x[i]=="0":
                    Flag=i
                    break
            if Flag:
                x[Flag],x[Flag+1]=x[Flag+1],x[Flag]
                x="".join(x)
            else:
                x="10"+"".join(x[1:])
            answer.append(int(x,2))
    return answer