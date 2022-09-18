import sys

N, M, L = map(int, sys.stdin.readline().split())
C = sorted(map(int, sys.stdin.readline().split()))
left = 0
P = []
if C:
    for c in C:
        P.append(c - left)
        left = c
    P.append(L - C[len(C) - 1])
else:
    P.append(L)

def calcN(target: int):
    n = 0
    for p in P:
        if p > target:
            n += (p - 1) // target
    return n

start, end = 0, max(P)
while start < end:
    mid = (start + end + 1) // 2
    count = calcN(mid)
    if count >= M + 1:
        start = mid
    else:
        end = mid - 1

print(start + 1)