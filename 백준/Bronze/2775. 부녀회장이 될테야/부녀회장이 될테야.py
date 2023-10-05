T = int(input())
for _ in range(T):
  k = int(input())
  n = int(input())
  floor = [1] * n
  for _ in range(k):
    for i in range(n):
        floor[i] = sum(floor[i:n])
  print(sum(floor))