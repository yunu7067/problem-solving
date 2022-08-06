import sys

N, K = map(int, sys.stdin.readline().split())
C = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
n = 0

while K != 0:
    if K < C[-1]:
        C.pop()
        continue
    K -= C[-1]
    n += 1

print(n)