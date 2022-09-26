from collections import deque
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    M, N, K = map(int, input().split())
    board = [[0] * M for _ in range(N)]
    earthworm = [[False] * M for _ in range(N)]
    Q = deque([])
    for _ in range(K):
        c, r = map(int, input().split())
        board[r][c] = 1
    dr, dc = [1, 0, -1, 0], [0, 1, 0, -1]
    worm_count = 0

    for r in range(N):
        for c in range(M):
            if board[r][c] == 1 and not earthworm[r][c]:
                worm_count += 1
                Q.append((r, c))
                earthworm[r][c] = True

                while Q:
                    cr, cc = Q.pop()
                    for i in range(4):
                        nr, nc = cr + dr[i], cc + dc[i]
                        if nr < 0 or nr >= N or nc < 0 or nc >= M:
                            continue
                        if board[nr][nc] == 1 and not earthworm[nr][nc]:
                            earthworm[nr][nc] = True
                            Q.append((nr, nc))

    print(worm_count)