import sys
input=sys.stdin.readline

N=int(input())
shirts=input().split()
T,P=map(int,input().split())
print(sum(map(lambda x: (x-1)//T+1,map(int,shirts))))
print(N//P,N%P)