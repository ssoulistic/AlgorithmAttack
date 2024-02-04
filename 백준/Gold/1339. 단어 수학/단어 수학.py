import sys
input=sys.stdin.readline
dic={}
add=[[] for _ in range(8)]
N=int(input())
for _ in range(N):
    word=input().strip()
    for w in range(len(word)):
        add[8-len(word)+w].append(word[w])
answer=0
number=9

# 우선 순위 배율 구하기
for digit in range(8):
    while add[digit]:
        alpha=add[digit].pop()
        if dic.get(alpha):
            dic[alpha]+=10**(7-digit)
        else:
            dic[alpha]=10**(7-digit)

# 순위에 따라 숫자 배정하여 계산하기.
answer=0
number=9
for i in sorted(dic.values(),reverse=True):
    answer+=number*i
    number-=1
print(answer)