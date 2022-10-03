from collections import deque
import sys

input = sys.stdin.readline
d = [[-2, -1], [-1, -2], [1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1]]
for _ in range(int(input())):
    L = int(input())  # 체스판 크기
    src = list(map(int, input().rstrip().split()))  # 시작 위치
    dest = list(map(int, input().rstrip().split()))  # 도착 위치
    if src == dest:
        print(0)
        continue

    visited = [[-1] * L for _ in range(L)]
    visited[src[0]][src[1]] = 0
    Q = deque([src])

    while Q:
        cr, cc = Q.popleft()
        if [cr, cc] == dest:
            print(visited[cr][cc])
            break
        for dr, dc in d:
            nr, nc = cr + dr, cc + dc
            if not (0 <= nr < L and 0 <= nc < L):
                continue
            if visited[nr][nc] == -1:
                Q.append([nr, nc])
                visited[nr][nc] = visited[cr][cc] + 1