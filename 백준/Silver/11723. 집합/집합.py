import sys
m=int(sys.stdin.readline())
S=set()
for _ in range(m):
    command=sys.stdin.readline().split()
    if command[0]=="add" and int(command[1]) not in S:
        S.add(int(command[1]))
    elif command[0]=="remove" and int(command[1]) in S:
        S.remove(int(command[1]))
    elif command[0]=="check":
        if int(command[1]) in S:
            print(1)
        else:
            print(0)
    elif command[0]=="toggle":
        if int(command[1]) in S:
            S.remove(int(command[1]))
        else:
            S.add(int(command[1]))
    elif command[0]=="all":
        S=set(i for i in range(1,21))
    elif command[0]=="empty":
        S=set()
