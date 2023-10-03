n=int(input())
answer=0
hello=set()
for _ in range(n):
    log=input()
    if log == "ENTER":
        hello=set()
    elif log not in hello:
        hello.add(log)
        answer+=1
print(answer)