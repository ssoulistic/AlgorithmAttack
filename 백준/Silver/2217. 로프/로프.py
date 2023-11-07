import sys
T=int(sys.stdin.readline())
rope=[]
for _ in range(T):
    rope.append(int(sys.stdin.readline()))
rope.sort()
maxi=0
for i in range(len(rope)):
    if maxi<rope[i]*(len(rope)-i):
        maxi=rope[i]*(len(rope)-i)
print(maxi)
    
