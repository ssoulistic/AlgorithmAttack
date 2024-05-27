import sys
input=sys.stdin.readline
eq=''
for _ in range(3):
    eq+=input().strip()
print(eval(eq))