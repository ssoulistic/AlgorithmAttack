def solution(A, B):
    N=len(A)
    answer = 0
    A.sort()
    B.sort()
    i,j=0,0
    while i<N and j<N:
        if A[i]<B[j]:
            answer+=1
            i+=1
            j+=1
        else:
            j+=1
    return answer