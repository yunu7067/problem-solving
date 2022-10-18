import sys

input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    B = [list(map(int, input().split())) + [0] for _ in range(2)]
    DP = [[0] * (N + 1) for _ in range(2)]
    DP[0][0], DP[1][0] = B[0][0], B[1][0]
    for i in range(N - 1):
        # 위
        DP[1][i + 1] = max(DP[1][i + 1], DP[0][i] + B[1][i + 1])
        DP[1][i + 2] = max(DP[1][i + 2], DP[0][i] + B[1][i + 2])
        # 아래
        DP[0][i + 1] = max(DP[0][i + 1], DP[1][i] + B[0][i + 1])
        DP[0][i + 2] = max(DP[0][i + 2], DP[1][i] + B[0][i + 2])

    print(max(DP[0][N - 1], DP[1][N - 1]))