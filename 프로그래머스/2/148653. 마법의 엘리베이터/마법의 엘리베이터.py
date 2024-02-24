def elv(num,count):
    if num==0:
        return count
    num,move=divmod(num,10)
    if move>5:
        count+=10-move
        num+=1
    elif move<5:
        count+=move
    elif move==5:
        count+=move
        if num % 10 >=5:
            num+=1
    return elv(num,count)

def solution(storey):
    # 자신이 5 => 다음 수가 5보다 커지면 올리는게 이득 5면 굳이..
    answer=elv(storey,0)  
    return answer