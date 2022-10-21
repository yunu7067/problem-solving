import sys

input = sys.stdin.readline
N, M = map(int, input().split())

B = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
Q = [list(map(int, input().split())) for _ in range(M)]

for r in range(1, N + 1):
    for c in range(1, N + 1):
        B[r][c] = B[r][c] + B[r][c - 1] + B[r - 1][c] - B[r - 1][c - 1]

for r1, c1, r2, c2 in Q:
    a = B[r2][c2] - B[r1 - 1][c2] - B[r2][c1 - 1] + B[r1 - 1][c1 - 1]
    print(a)