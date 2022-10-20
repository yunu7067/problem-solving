import sys

input = sys.stdin.readline
N = int(input())
B = [int(input()) for _ in range(N)]
DP = [[0] * 3 for _ in range(N)]
DP[0][1] = B[0]
for idx in range(1, N):
    DP[idx][0] = max(DP[idx - 1])
    DP[idx][1] = DP[idx - 1][0] + B[idx]
    DP[idx][2] = DP[idx - 1][1] + B[idx]

print(max(DP[N - 1]))