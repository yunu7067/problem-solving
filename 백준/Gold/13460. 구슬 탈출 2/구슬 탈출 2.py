import sys
from typing import List

input = sys.stdin.readline
N, M = map(int, input().split())
board = []
red_ball, blue_ball, hole = None, None, None
for _r in range(N):
    _row = input().rstrip()
    for _c in range(M):
        if _row[_c] == "O":
            hole = [_r, _c]
        elif _row[_c] == "R":
            red_ball = [_r, _c]
        elif _row[_c] == "B":
            blue_ball = [_r, _c]
    board.append([*_row])

# 0 : 왼쪽
# 1 : 위
# 2 : 오른쪽
# 3 : 아래
d = [[0, -1], [-1, 0], [0, 1], [1, 0]]

def move_ball(
    ball: List[int],
    balls: List[List[int]],
    direction: int,
):
    global board, hole
    cr, cc = ball
    dr, dc = d[direction]

    while True:
        nr, nc = cr + dr, cc + dc

        if board[nr][nc] == "#" or ([nr, nc] != hole and [nr, nc] in balls):
            return [cr, cc]
        elif [nr, nc] == hole:
            return [nr, nc]
        else:
            cr, cc = nr, nc

def move_balls(rball, bball, direction: int):
    total_balls = [[rball, "R"], [bball, "B"]]
    # 방향에 맞게 정렬
    total_balls.sort(
        key=lambda x: x[0][0 if direction == 1 or direction == 3 else 1],
        reverse=(direction == 2 or direction == 3),
    )

    mvd_rball, mvd_bball = rball, bball
    for pos, color in total_balls:
        if color == "R":
            mvd_rball = move_ball(pos, [mvd_rball, mvd_bball], direction)
        else:
            mvd_bball = move_ball(pos, [mvd_rball, mvd_bball], direction)

    return (mvd_rball, mvd_bball)

counts = []

def calc(cnt: int, rball: List[int], bball: List[int]):
    if cnt >= 10:
        return False
    for direction in range(4):
        mvd_rball, mvd_bball = move_balls(rball, bball, direction)
        if hole == mvd_bball:
            continue
        if hole == mvd_rball:
            counts.append(cnt + 1)
        if not (rball == mvd_rball and bball == mvd_bball) and hole != mvd_rball:
            calc(cnt + 1, mvd_rball, mvd_bball)
    return 0

calc(0, red_ball, blue_ball)
print(min(counts) if counts else -1)