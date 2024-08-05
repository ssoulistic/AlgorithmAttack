import sys
input=sys.stdin.readline
N=int(input())

TS=[[0,0] for _ in range(366)]
conv = {"T":0,"S":1}
a1,a2,a3,a4,a5=0,0,0,0,0
for _ in range(N):
  c,s,e=input().split()
  if a5<(int(e)-int(s)+1):
    a5=int(e)-int(s)+1
  for i in range(int(s),int(e)+1):
    TS[i-1][conv[c]]+=1


for j in range(366):
  sub_sum=sum(TS[j])
  if(sub_sum)>=1:
    a1+=1
  if sub_sum>a2:
    a2=sub_sum
  if TS[j][0]==TS[j][1]!=0:
    a3+=1
    if a4<sub_sum:
      a4=sub_sum
print(a1)
print(a2)
print(a3)
print(a4)
print(a5)