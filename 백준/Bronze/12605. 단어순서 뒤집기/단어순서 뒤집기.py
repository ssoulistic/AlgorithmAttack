import sys
input=sys.stdin.readline
N=int(input())
for i in range(N):
    sentence=input().split()
    print(f"Case #{i+1}: {' '.join(sentence[::-1])}")