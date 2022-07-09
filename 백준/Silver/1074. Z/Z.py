import sys

def Z(n, p):
    if n == 0:
        return 0
    next_half = 1 << n - 1
    if p[0] < next_half and p[1] < next_half:
        return Z(n - 1, (p[0], p[1]))
    if p[0] < next_half and p[1] >= next_half:
        return 1 * next_half * next_half + Z(n - 1, (p[0], p[1] - next_half))
    if p[0] >= next_half and p[1] < next_half:
        return 2 * next_half * next_half + Z(n - 1, (p[0] - next_half, p[1]))
    return 3 * next_half * next_half + Z(n - 1, (p[0] - next_half, p[1] - next_half))

N, r, c = map(int, sys.stdin.readline().split())
print(Z(N, (r, c)))