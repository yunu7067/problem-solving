import sys

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
d = [0]
for i, num in enumerate(nums):
    d.append(d[i] + num)

for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    print(d[e] - d[s - 1])