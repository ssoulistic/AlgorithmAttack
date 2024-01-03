import sys
T=int(sys.stdin.readline())

for _ in range(T):
    command=sys.stdin.readline()
    n=int(sys.stdin.readline())
    xs=eval(sys.stdin.readline())
    answer=xs
    reverse=False
    for com in command:
        if com=="R":
            if reverse:
                reverse=False
            else:
                reverse=True
        elif com=="D":
            if answer:
                if reverse: 
                    answer.pop()
                else:
                    answer.pop(0)
            else:
                answer="error"
                break
    if answer!="error" and reverse:
        answer.reverse()
    if answer=="error":
        print(answer)
    else:
        print("["+",".join(map(str,answer))+"]")
            
            


