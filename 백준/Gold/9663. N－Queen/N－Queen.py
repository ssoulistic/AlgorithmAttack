T=int(input())
result=[]
count=0
def queen(col):
    global count
    if len(result)==T:
        count+=1
        return 
    if col>=T:
        return
    # 위에서 부터 시작.
    for row in range(T):
        check=True
        # 한개 선택 => 아래로 있는지 체크, 좌대각 우대각 체크 좌표로 넣기.
        if result:
            for x,y in result:
                if y==row or abs(x-col)==abs(y-row):
                    check=False
                    break
        if check:
            result.append([col,row])
            queen(col+1)
            result.pop()
queen(0)
print(count)