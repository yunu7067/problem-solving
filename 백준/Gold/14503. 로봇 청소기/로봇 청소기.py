import sys

input = sys.stdin.readline
N, M = map(int, input().split())
r, c, d = map(int, input().split())
# 0: 빈 칸, 1: 벽, -1: 방문함
board = [list(map(int, input().split())) for _ in range(N)]
dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def clean():
    global r, c, d
    while True:
        if board[r][c] == 0:
            board[r][c] = -1
        is_all_clean = True
        for i in map(lambda x: x % 4, range(d + 3, d - 1, -1)):
            nr, nc = r + dirs[i][0], c + dirs[i][1]
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if board[nr][nc] == 0:
                board[nr][nc] = -1
                is_all_clean = False
                r, c, d = nr, nc, i  # 위치, 방향 설정
                break
        if is_all_clean:
            nr, nc = r - dirs[d][0], c - dirs[d][1]
            # 벽이면 종료
            if not (0 <= nr < N and 0 <= nc < M) or board[nr][nc] == 1:
                print(sum([row.count(-1) for row in board]))
                exit()
            # 후진
            else:
                r, c = nr, nc

clean()