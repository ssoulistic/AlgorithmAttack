#브루트포스 풀이
import sys
target=int(sys.stdin.readline())
start=100
broke=int(sys.stdin.readline())
broken_numbers=list(map(int,sys.stdin.readline().split()))
rmc=[i for i in range(10)]
for num in broken_numbers:
    rmc.remove(num)

answer=abs(target-start)
for n in range(1000001):
    Flag=True
    for ni in str(n):
        if int(ni) not in rmc:
            Flag=False
            break
    if Flag:
        answer=min(answer,abs(n-target)+len(str(n)))
print(answer)    

# # 가장 가까운수 만들기. 백트래킹 풀이
# target=int(input())
# start=100
# broke=int(input())
# broken_numbers=list(map(int,input().split()))
# rmc=[i for i in range(10)]
# for num in broken_numbers:
#     rmc.remove(num)

# answer=abs(target-start)
# def backt(guess,finish):
#     global answer
#     if finish<=0:
#         return
#     if len(guess)==finish:
#         gn=int("".join(guess))
#         if answer>abs(target-gn)+len(str(gn)):
#             answer=abs(target-gn)+len(str(gn))
#         return
#     for r in rmc:
#         guess.append(str(r))
#         backt(guess,finish)
#         guess.pop()
#     return

# backt([],len(str(target))-1)
# backt([],len(str(target)))
# backt([],len(str(target))+1)

# print(answer)
