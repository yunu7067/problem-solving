import sys

N = int(sys.stdin.readline().rstrip())
queens = []

def NQueen(row: int):
    if row == N:
        return 1
    case = 0
    cur_row = [True] * N  # 현재 줄에서 갈 수 있는 칸
    for (queen_r, queen_c) in queens:
        move_c = row - queen_r
        # ↓ 방향 (+n, 0)
        cur_row[queen_c] = False
        # ↙ 방향 (+n, -n)
        if queen_c - move_c >= 0:
            cur_row[queen_c - move_c] = False
        # ↘︎ 방향 (+n, +n)
        if queen_c + move_c < N:
            cur_row[queen_c + move_c] = False
    # 모두 놓을 수 없다면
    if sum(cur_row) == 0:
        return 0

    for col, val in enumerate(cur_row):
        # 가능한 위치인 지 체크
        if not val:
            continue
        pos = (row, col)
        queens.append(pos)
        case += NQueen(row + 1)
        queens.pop()

    return case

print(NQueen(0))