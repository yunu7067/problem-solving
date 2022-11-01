from collections import deque
import sys
input = sys.stdin.readline

N, K = int(input()), int(input())
board = [[0] * N for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 1

L = int(input())  # 방향 변환 횟수
rotations = deque()
for _ in range(L):
    _next_time, _direction = input().split()
    rotations.append([int(_next_time), _direction])
# init
board[0][0] = 2
d = [[0, -1], [-1, 0], [0, 1], [1, 0]]  # [왼쪽, 위, 오른쪽, 아래]
snake, snake_direction = deque([[0, 0]]), 2
time = 0
while snake and time < 1_000_101:
    time += 1
    cr, cc = snake.pop()
    board[cr][cc] = 2
    snake.append([cr, cc])
    nr, nc = cr + d[snake_direction][0], cc + d[snake_direction][1]

    if not (0 <= nr < N and 0 <= nc < N) or board[nr][nc] == 2:  # 몸통
        print(time)
        exit()
    elif board[nr][nc] == 0:  # 빈칸
        pr, pc = snake.popleft()
        board[pr][pc] = 0

    snake.append([nr, nc])
    # 방향 전환
    if rotations and rotations[0][0] <= time:
        [_, direction] = rotations.popleft()
        if direction == "D":
            snake_direction = (snake_direction + 1) % 4
        else:
            snake_direction = (snake_direction - 1) % 4