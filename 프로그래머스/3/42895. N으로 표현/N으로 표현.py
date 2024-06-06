def solution(N, number):
    if N == number:
        return 1

    # DP 테이블 초기화
    dp = [set() for _ in range(9)]  # dp[i]는 N을 i번 사용해서 만들 수 있는 숫자들의 집합
    
    # dp[1]은 N 하나로만 구성된 집합
    dp[1].add(N)
    
    for i in range(2, 9):  # N을 2번부터 8번까지 사용하는 경우
        # 숫자 반복으로 만든 수 (N, NN, NNN, ...)
        dp[i].add(int(str(N) * i))
        
        for j in range(1, i):
            for op1 in dp[j]:
                for op2 in dp[i - j]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)
        
        # 목표 숫자를 찾으면 반환
        if number in dp[i]:
            return i
    
    return -1
