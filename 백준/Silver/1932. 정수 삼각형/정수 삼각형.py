from collections import defaultdict, deque
import sys

# from heapq import heappop, heappush

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
DP = [[0] * N for _ in range(N)]
DP[N - 1] = board[N - 1]

for layer in range(N - 2, -1, -1):
    for idx, cur in enumerate(board[layer]):
        DP[layer][idx] = cur + max(DP[layer + 1][idx], DP[layer + 1][idx + 1])

print(DP[0][0])