import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
J_stack, F_stack = deque(), deque()
J_board = [[sys.maxsize] * C for _ in range(R)]
F_board = [[sys.maxsize] * C for _ in range(R)]
dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]

for r1 in range(R):
    for c1 in range(C):
        if board[r1][c1] == "J":
            J_board[r1][c1] = 0
            J_stack.append((r1, c1))
        elif board[r1][c1] == "F":
            F_board[r1][c1] = 0
            F_stack.append((r1, c1))

while F_stack:
    (r, c) = F_stack.popleft()
    for i in range(4):
        n_r, n_c = r + dr[i], c + dc[i]
        if (
            (0 <= n_r < R)
            and (0 <= n_c < C)
            and board[n_r][n_c] in (".", "J")
            and F_board[n_r][n_c] == sys.maxsize
        ):
            F_stack.append((n_r, n_c))
            F_board[n_r][n_c] = F_board[r][c] + 1

while J_stack:
    (r, c) = J_stack.popleft()
    for i in range(4):
        n_r, n_c = r + dr[i], c + dc[i]

        if (0 > n_r or n_r >= R) or (0 > n_c or n_c >= C):
            print(J_board[r][c] + 1)
            exit(0)
        if (
            (0 <= n_r < R)
            and (0 <= n_c < C)
            and board[n_r][n_c] == "."
            and J_board[n_r][n_c] == sys.maxsize
            and J_board[r][c] + 1 < F_board[n_r][n_c]
        ):
            J_stack.append((n_r, n_c))
            J_board[n_r][n_c] = J_board[r][c] + 1

print("IMPOSSIBLE")
