import sys
N = int(sys.stdin.readline())
DP = [[0] * 10 for _ in range(N + 1)]
for i in range(10):
    DP[1][i] = 1

for j in range(2, N + 1):
    for n in range(10):
        DP[j][n] = DP[j - 1][n] + sum(DP[j - 1][n + 1 :])

print(sum(DP[N]) % 10_007)