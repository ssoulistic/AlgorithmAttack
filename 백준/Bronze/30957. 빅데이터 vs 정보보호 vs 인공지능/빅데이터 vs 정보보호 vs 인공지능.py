import sys
T=int(sys.stdin.readline().strip())
word=sys.stdin.readline().strip()
B=word.count("B")
S=word.count("S")
A=word.count("A")
t=max(B,S,A)
answer=""
if t==B:
    answer+="B"
if t==S:
    answer+="S"
if t==A:
    answer+="A"
if answer=="BSA":
    print("SCU")
else:
    print(answer)