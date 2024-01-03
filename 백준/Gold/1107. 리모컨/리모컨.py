import sys
target=int(sys.stdin.readline())
start=100
broke=int(sys.stdin.readline())
broken_numbers=list(map(int,sys.stdin.readline().split()))
rmc=[i for i in range(10)]
for num in broken_numbers:
    rmc.remove(num)

def click_able(n):
    for s in str(n):
        if int(s) not in rmc:
            return False
    return True

# 가장 가까운수 만들기. 백트래킹 ㄱ
answer=abs(target-start)
def backt(guess,finish):
    global answer
    if finish<=0:
        return
    if len(guess)==finish:
        gn=int("".join(guess))
        if answer>abs(target-gn)+len(str(gn)):
            answer=abs(target-gn)+len(str(gn))
        return
    for r in rmc:
        guess.append(str(r))
        backt(guess,finish)
        guess.pop()
    return

backt([],len(str(target))-1)
backt([],len(str(target)))
backt([],len(str(target))+1)

print(answer)