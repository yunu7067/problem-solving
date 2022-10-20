import sys

input = sys.stdin.readline
N = int(input())
DP = [[0] * 10 for _ in range(N + 1)]
for i in range(1, 10):
    DP[1][i] = 1

for idx in range(2, N + 1):
    for i in range(10):
        if i == 0:
            DP[idx][i] = DP[idx - 1][i + 1]
        elif i == 9:
            DP[idx][i] = DP[idx - 1][i - 1]
        else:
            DP[idx][i] = DP[idx - 1][i - 1] + DP[idx - 1][i + 1]

print(sum(DP[N]) % 1_000_000_000)