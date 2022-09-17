from math import lcm
import sys

def b6464(M: int, N: int, x: int, y: int):
    if M == x:
        x = 0
    if N == y:
        y = 0
    for i in range(x, lcm(M, N) + 1, M):
        if i == 0:
            continue
        if i % N == y:
            return i
    return -1

N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    M, N, x, y = map(int, sys.stdin.readline().split())
    print(b6464(M, N, x, y))