from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
stack = deque([(0, 0, 0)])
count_board = [[0] * M for _ in range(N)]

while stack:
    r, c, prev_hop = stack.popleft()
    cur_hop = prev_hop + 1
    if count_board[r][c] == 0 or count_board[r][c] > cur_hop:
        count_board[r][c] = cur_hop
    else:
        continue
    # 왼쪽
    if c - 1 >= 0 and board[r][c - 1] == 1 and count_board[r][c - 1] == 0:
        stack.append((r, c - 1, cur_hop))
    # 위
    if r - 1 >= 0 and board[r - 1][c] == 1 and count_board[r - 1][c] == 0:
        stack.append((r - 1, c, cur_hop))
    # 오른쪽
    if c + 1 < M and board[r][c + 1] == 1 and count_board[r][c + 1] == 0:
        stack.append((r, c + 1, cur_hop))
    # 아래
    if r + 1 < N and board[r + 1][c] == 1 and count_board[r + 1][c] == 0:
        stack.append((r + 1, c, cur_hop))

print(count_board[N - 1][M - 1])
