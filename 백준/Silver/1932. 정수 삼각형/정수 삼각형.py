import sys
input = sys.stdin.readline
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
for layer in range(N - 2, -1, -1):
    for idx, cur in enumerate(board[layer]):
        board[layer][idx] = cur + max(board[layer + 1][idx], board[layer + 1][idx + 1])

print(board[0][0])