def solution(triangle):
    mem=[0 for _ in range(len(triangle)+2)]
    for seq in range(len(triangle)):
        temp=[]
        for i in range(len(triangle[seq])):
            temp.append(max(mem[i],mem[i+1])+triangle[seq][i])
        for j in range(len(temp)):
            mem[j+1]=temp[j]
    return max(mem)