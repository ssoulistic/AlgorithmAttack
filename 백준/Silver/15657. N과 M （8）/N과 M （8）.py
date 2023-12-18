import sys
N,M=map(int,sys.stdin.readline().strip().split())
given=sorted(map(int,sys.stdin.readline().strip().split()))

def backtrack(sequence,depth):
    if depth==M:
        print(*sequence)
        return
    for g in given:
        if sequence ==[] or sequence[-1]<=g:
            sequence.append(g)
            backtrack(sequence,depth+1)
            sequence.pop()
backtrack([],0)