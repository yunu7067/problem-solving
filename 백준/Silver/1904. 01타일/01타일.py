import sys

N = int(sys.stdin.readline())
DP = [0] * (N + 1)
DP[0], DP[1] = 1, 1
for n in range(2, N + 1):
    DP[n] = (DP[n - 1] + DP[n - 2]) % 15746
print(DP[N])