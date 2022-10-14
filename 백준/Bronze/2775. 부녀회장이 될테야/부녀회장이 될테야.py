import sys
input = sys.stdin.readline

N = int(input())
aprt = [[0] * 15 for _ in range(15)]
aprt[0] = [i for i in range(15)]

for r in range(1, 15):
    for c in range(1, 15):
        aprt[r][c] = aprt[r][c - 1] + aprt[r - 1][c]

for _ in range(N):
    k, n = int(input()), int(input())
    print(aprt[k][n])