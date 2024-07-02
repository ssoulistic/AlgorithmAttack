import sys
input=sys.stdin.readline
emoji=input().strip()
print(len(emoji)+emoji.count(":")+emoji.count("_")*5)