from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
B, L = [], []
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
w_visited = [[False] * C for _ in range(R)]
wc_Q, wn_Q = deque(), deque()
s_visited = [[False] * C for _ in range(R)]
sc_Q, sn_Q = deque(), deque()

def init_board():
    for _r in range(R):
        _row = list(input().rstrip())
        for _c, _v in enumerate(_row):
            if _v == "L":
                L.append([_r, _c])
        B.append(_row)

def init_water_bfs():
    for _r in range(R):
        for _c in range(C):
            if B[_r][_c] != "X" and not w_visited[_r][_c]:
                w_visited[_r][_c] = True
                wc_Q.append([_r, _c])
            while wc_Q:
                cr, cc = wc_Q.popleft()
                for dr, dc in d:
                    nr, nc = cr + dr, cc + dc
                    if not (0 <= nr < R and 0 <= nc < C):
                        continue
                    if not w_visited[nr][nc]:
                        w_visited[nr][nc] = True
                        if B[nr][nc] != "X":
                            wc_Q.append([nr, nc])
                        else:
                            wn_Q.append([nr, nc])

def init_swan_bfs():
    sc_Q.append(L[0])
    s_visited[L[0][0]][L[0][1]] = True
    while sc_Q:
        cr, cc = sc_Q.popleft()
        for dr, dc in d:
            nr, nc = cr + dr, cc + dc
            if not (0 <= nr < R and 0 <= nc < C):
                continue
            if not s_visited[nr][nc]:
                s_visited[nr][nc] = True
                if B[nr][nc] == "X":
                    sn_Q.append([nr, nc])
                elif B[nr][nc] == "L":
                    print(0)
                    exit()
                else:
                    sc_Q.append([nr, nc])

init_board()
init_water_bfs()
init_swan_bfs()

for time in range(1, 3001):
    wc_Q, wn_Q = wn_Q, wc_Q
    sc_Q, sn_Q = sn_Q, sc_Q

    # 물 탐색
    while wc_Q:
        cr, cc = wc_Q.popleft()
        B[cr][cc] = "."
        for dr, dc in d:
            nr, nc = cr + dr, cc + dc
            if not (0 <= nr < R and 0 <= nc < C):
                continue
            if not w_visited[nr][nc]:
                w_visited[nr][nc] = True
                if B[nr][nc] == "X":
                    wn_Q.append([nr, nc])
    # 백조 탐색
    while sc_Q:
        cr, cc = sc_Q.popleft()
        for dr, dc in d:
            nr, nc = cr + dr, cc + dc
            if not (0 <= nr < R and 0 <= nc < C):
                continue
            if not s_visited[nr][nc]:
                s_visited[nr][nc] = True
                if B[nr][nc] == "X":
                    sn_Q.append([nr, nc])
                elif B[nr][nc] == "L":
                    print(time)
                    exit()
                else:
                    sc_Q.append([nr, nc])