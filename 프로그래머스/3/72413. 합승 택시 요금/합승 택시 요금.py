def solution(n, s, a, b, fares):
    floyd=[[1e9 for _ in range(n)] for _ in range(n)]
    # 경유점=>A,B까지의 거리 최소값.
    for i in range(n):
        floyd[i][i]=0
    for start,end,cost in fares:
        floyd[start-1][end-1]=cost
        floyd[end-1][start-1]=cost
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if floyd[i][k]+floyd[k][j]<floyd[i][j]:
                    floyd[i][j]=floyd[i][k]+floyd[k][j]

    answer = 1e9
    for l in range(n):
        if answer>(floyd[s-1][l]+floyd[l][a-1]+floyd[l][b-1]):
            answer=(floyd[s-1][l]+floyd[l][a-1]+floyd[l][b-1])
    return answer