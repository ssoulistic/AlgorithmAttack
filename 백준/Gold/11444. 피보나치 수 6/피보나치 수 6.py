num=int(input())
A=[[0,1],[1,1]]
p=1000000007
def multiply(matrix1,matrix2):
    answer=[[0 for _ in range(2)]for _ in range(2)]
    mlen=len(matrix1)
    for i in range(mlen):
        for j in range(mlen):
            for k in range(mlen):
                answer[i][j]+=matrix1[i][k]*matrix2[k][j] % p
            answer[i][j]%=p
    return answer

def fibo(matrix,repeat):
    if repeat<=1:
        return matrix
    if repeat % 2 ==1:
        return multiply(fibo(multiply(matrix,matrix),(repeat-1)//2),matrix)
    else:
        return fibo(multiply(matrix,matrix),repeat//2)
print(fibo(A,num+1)[0][0])