import sys

N = int(sys.stdin.readline().rstrip())
P = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
d = [[-1] * 3 for _ in range(N)]

d[0][0], d[0][1], d[0][2] = P[0]

if N == 1:
    print(min(P[0]))
    exit(0)

for i in range(1, N):
    r, g, b = d[i - 1]
    d[i][0], d[i][1], d[i][2] = (
        P[i][0] + min([g, b]),
        P[i][1] + min([r, b]),
        P[i][2] + min([r, g]),
    )

print(min(d[N - 1]))