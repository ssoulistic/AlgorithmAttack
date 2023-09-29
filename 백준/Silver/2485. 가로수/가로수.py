import sys
import math
n=int(sys.stdin.readline())
# n=int(input())
x1=int(sys.stdin.readline())
# x1=int(input())
trees=[x1]
far=[]
for i in range(n-1):
    x2=int(sys.stdin.readline())
    # x2=int(input())
    trees.append(x2)
    far.append(x2-x1)
    x1=x2

gap=math.gcd(*far)
answer=(trees[-1]-trees[0]) // gap - (len(trees)-1)
print(answer)