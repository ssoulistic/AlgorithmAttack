  
def solution(arr1, arr2):
    row1=len(arr1)
    col1=len(arr1[0])
    row2=len(arr2)
    col2=len(arr2[0])
    answer = [[None for i in range(col2)] for j in range(row1)]
    for i in range(row1):
        for j in range(col2):
            temp=0
            for k in range(row2):
                # print(arr1[i][k],arr2[k][j])
                temp+=arr1[i][k]*arr2[k][j]
            answer[i][j]=(temp)
            # print(i,j,temp,answer)
            
    return answer