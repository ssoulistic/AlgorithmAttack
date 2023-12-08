def solution(n, k):
    result = []
    numbers = list(range(1, n + 1))

    k -= 1  # 인덱스를 0부터 시작하도록 조정
    factorial = 1

    # 팩토리얼 계산
    for i in range(1, n + 1):
        factorial *= i

    for i in range(n, 0, -1):
        factorial //= i
        index = k // factorial
        k %= factorial
        result.append(numbers.pop(index))

    return result