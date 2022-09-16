import sys

N, K = map(int, sys.stdin.readline().split())
M = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
P = [[-sys.maxsize for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(N + 1):
    P[i][0] = 0
for j in range(1, K + 1):
    P[0][j] = 0

for i in range(1, N + 1):
    for w in range(1, K + 1):
        P[i][w] = P[i - 1][w] if M[i - 1][0] > w else max(P[i - 1][w], M[i - 1][1] + P[i - 1][w - M[i - 1][0]])

print(P[N][K])