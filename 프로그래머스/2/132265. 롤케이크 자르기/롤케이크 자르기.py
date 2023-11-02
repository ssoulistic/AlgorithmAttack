def solution(topping):
    count=0
    counter=[[0,0] for _ in range(len(topping))]
    front=set()
    back=set()
    for i in range(len(topping)):
        front.add(topping[i])
        back.add(topping[len(topping)-1-i])
        counter[i][0]=len(front)
        counter[len(topping)-1-i][1]=len(back)
    for j in range(len(counter)-1):
        if counter[j][0]==counter[j+1][1]:
            count+=1
    return(count)