import sys
N,M=map(int,input().split())
dic={}
for i in range(1,N+1):
    name=sys.stdin.readline().rstrip()
    dic[str(i)]=name
    dic[name]=str(i)
for _ in range(M):
    question=sys.stdin.readline().rstrip()
    print(dic[question])