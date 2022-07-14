import sys
from typing import List

N, M, K = map(int, sys.stdin.readline().split())
board = [[False] * M for _ in range(N)]

# 배열을 90도 회전시킨 후 반환한다.
def rotate(matrix: List):
    return [[row[i] for row in matrix[::-1]] for i in range(len(matrix[0]))]

def count_board():
    count = 0
    for row in board:
        for value in row:
            if value:
                count += 1
    return count

# 배열에 해당 스티커를 붙일 수 있는지 체크 후 결과를 반환한다.
def stick(n: int, m: int, matrix: List):
    matrix_R = len(matrix)
    matrix_C = len(matrix[0])
    matrix_size = matrix_R * matrix_C
    for r in range(0, n - matrix_R + 1):
        for c in range(0, m - matrix_C + 1):
            # 붙일 수 있는지 전부 탐색
            count = 0
            for st_r in range(0, matrix_R):
                for st_c in range(0, matrix_C):
                    a = not (matrix[st_r][st_c] == 1 and board[r + st_r][c + st_c])
                    if not (matrix[st_r][st_c] == 1 and board[r + st_r][c + st_c]):
                        count += 1
                    else:
                        break
            if count == matrix_size:
                for st_r in range(0, matrix_R):
                    for st_c in range(0, matrix_C):
                        board[r + st_r][c + st_c] = (
                            board[r + st_r][c + st_c] or matrix[st_r][st_c] == 1
                        )
                return True
    return False

for k in range(K):
    sticker_R, sticker_C = map(int, sys.stdin.readline().split())
    sticker = [list(map(int, sys.stdin.readline().split())) for _ in range(sticker_R)]
    if not stick(N, M, sticker):
        sticker_deg90 = rotate(sticker)
        if not stick(N, M, sticker_deg90):
            sticker_deg180 = rotate(sticker_deg90)
            if not stick(N, M, sticker_deg180):
                sticker_deg270 = rotate(sticker_deg180)
                if not stick(N, M, sticker_deg270):
                    continue

print(count_board())