import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
count_board = [[0] * M for _ in range(N)]
stack = deque()

for row in range(0, N):
    for col in range(0, M):
        if board[row][col] == 1:
            stack.append((row, col, -1))
while stack:
    (r, c, prev_hop) = stack.popleft()
    cur_hop = prev_hop + 1
    if count_board[r][c] == 0 or count_board[r][c] > cur_hop:
        count_board[r][c] = cur_hop
    else:
        continue
    # 왼쪽
    if c - 1 >= 0 and board[r][c - 1] == 0 and count_board[r][c - 1] == 0:
        stack.append((r, c - 1, cur_hop))
    # 위쪽
    if r - 1 >= 0 and board[r - 1][c] == 0 and (count_board[r - 1][c] == 0):
        stack.append((r - 1, c, cur_hop))
    # 오른쪽
    if c + 1 < M and board[r][c + 1] == 0 and (count_board[r][c + 1] == 0):
        stack.append((r, c + 1, cur_hop))
    # 아래쪽
    if r + 1 < N and board[r + 1][c] == 0 and (count_board[r + 1][c] == 0):
        stack.append((r + 1, c, cur_hop))

# 토마토 체크
max_hop = 0
for row in range(0, N):
    for col in range(0, M):
        if count_board[row][col] == 0 and board[row][col] == 0:
            print(-1)
            exit(0)
        else:
            if max_hop < count_board[row][col]:
                max_hop = count_board[row][col]

print(max_hop)
