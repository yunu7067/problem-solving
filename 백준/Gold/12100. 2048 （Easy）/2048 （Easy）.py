import sys
from typing import List

N = int(sys.stdin.readline().rstrip())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 말판을 90도 회전시킨다
def rotate():
    return [[row[i] for row in board[::-1]] for i in range(len(board[0]))]

# 현재 말판의 최댓값
def max_board():
    _max = 0
    for _row in board:
        _max = max(_row) if max(_row) > _max else _max
    return _max

# 말판 깊은복사
def board_copy():
    return [_row[:] for _row in board]

# 왼쪽으로 병합
def slice_right_to_left():
    for i, _ in enumerate(board):
        board[i] = merge_row(board[i])

# 한 줄 병합
def merge_row(arr: List):
    length = len(arr)
    moved = [0] * length
    merged = [0] * length
    # 왼쪽으로 빈 칸(0)이 없게 이동
    i = 0
    for num in arr:
        if num != 0:
            moved[i] = num
            i += 1
    i = 0
    last = 0
    # 왼쪽부터 병합
    while True:
        if i >= length or moved[i] == 0:
            break
        if i < length - 1 and moved[i] == moved[i + 1]:
            merged[last] = moved[i] << 1
            i += 2
            last += 1
        else:
            merged[last] = moved[i]
            i += 1
            last += 1

    return merged

max_num = 0

def func(n):
    global board, max_num

    if n == 5:
        cur_max = max_board()
        if cur_max > max_num:
            max_num = cur_max
        return

    temp_board = board_copy()  # 말판 복사

    for i in range(4):
        for _ in range(i):
            board = rotate()
        slice_right_to_left()
        func(n + 1)
        board = temp_board  # 말판 복원

func(0)
print(max_num)