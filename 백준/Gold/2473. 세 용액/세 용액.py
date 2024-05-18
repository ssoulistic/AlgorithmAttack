import sys
input = sys.stdin.readline

# 입력 받기
N = int(input())
liq = list(map(int, input().split()))
liq.sort()  # 정렬

minimum = float('inf')  # 최소 절대값을 큰 값으로 초기화
result = []  # 결과 저장용 리스트

# 고정된 용액 a를 선택하고 나머지 두 용액을 투 포인터로 찾음
for i in range(N-2):
    left = i + 1
    right = N - 1
    
    while left < right:
        mix = liq[i] + liq[left] + liq[right]
        
        # 최소 절대값 갱신
        if abs(mix) < minimum:
            minimum = abs(mix)
            result = [liq[i], liq[left], liq[right]]
        
        # 특성값이 0에 가까워지도록 포인터 이동
        if mix < 0:
            left += 1
        else:
            right -= 1

# 결과 출력
print(*result)
