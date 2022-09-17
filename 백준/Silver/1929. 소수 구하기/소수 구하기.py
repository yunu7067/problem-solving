import sys

N, M = map(int, sys.stdin.readline().split())
D = [True] * (M + 1)
D[0], D[1] = False, False
for i in range(2, M + 1):
    if not D[i]:
        continue
    for n in range(i * i, M + 1, i):
        D[n] = False
    if N <= i <= M:
        print(i)