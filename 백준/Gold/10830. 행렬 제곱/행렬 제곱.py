import sys
N,B=map(int,sys.stdin.readline().split())
A=[]
p=1000
for _ in range(N):
    A.append(list(map(lambda x: int(x) % p,sys.stdin.readline().split())))

# 행렬의 곱
def multiply(matrix1,matrix2):
    answer=[[0 for _ in range(N)]for _ in range(N)]
    mlen=len(matrix1)
    for i in range(mlen):
        for j in range(mlen):
            for k in range(mlen):
                answer[i][j]+=matrix1[i][k]*matrix2[k][j] % p
            answer[i][j]%=p
    return answer

def square(matrix,repeat):
    if repeat<=1:
        return matrix
    if repeat % 2 ==1:
        return multiply(matrix,square(multiply(matrix,matrix),(repeat-1)//2))
    else:
        return square(multiply(matrix,matrix),(repeat//2))
for s in square(A,B):
    print(*s)