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

    visited = [[False] * L for _ in range(L)]
    visited[src[0]][src[1]] = True
    Q = deque([(*src, 0)])

    while Q:
        cr, cc, chop = Q.popleft()
        for dr, dc in d:
            nr, nc, nhop = cr + dr, cc + dc, chop + 1
            if not (0 <= nr < L and 0 <= nc < L):
                continue
            if [nr, nc] == dest:
                print(nhop)
                Q = []
                break
            if not visited[nr][nc]:
                Q.append((nr, nc, nhop))
                visited[nr][nc] = True