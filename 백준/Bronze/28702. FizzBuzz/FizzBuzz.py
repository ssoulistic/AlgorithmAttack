import sys
input=sys.stdin.readline

A=input().strip()
B=input().strip()
C=input().strip()
next_num=0

if A.isdigit():
  next_num=int(A)+3
elif B.isdigit():
  next_num=int(B)+2
elif C.isdigit():
  next_num=int(C)+1

if next_num % 3 ==0 and next_num % 5 ==0 :
  print("FizzBuzz")
elif next_num % 3 ==0:
  print("Fizz")
elif  next_num % 5 ==0:
  print("Buzz")
else:
  print(next_num)
