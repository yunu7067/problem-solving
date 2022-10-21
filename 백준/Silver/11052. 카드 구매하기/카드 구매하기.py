import sys

input = sys.stdin.readline
N = int(input())
P = [0] + list(map(int, input().split()))
DP = P.copy()

for p in range(1, N + 1):
    for i in range(1, p + 1):
        DP[p] = max(DP[p], DP[p - i] + P[i])

print(DP[N])