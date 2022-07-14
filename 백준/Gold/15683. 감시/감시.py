import sys

N, M = map(int, sys.stdin.readline().split())
office = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# CCTV 위치 구하기
cctvs = []
for _r in range(N):
    for _c in range(M):
        if 0 < office[_r][_c] < 6:
            cctvs.append((office[_r][_c], _r, _c))
cctvs.sort(key=lambda x: -x[0])
arr = [-1] * len(cctvs)
visited = [False] * len(cctvs)


def calc_blindspots():
    cur_blindspots = 0
    for _r in range(N):
        for _c in range(M):
            if office[_r][_c] == 0:
                cur_blindspots += 1
    return cur_blindspots


# cctv가 하나도 없는 경우
if len(cctvs) == 0:
    print(calc_blindspots())
    exit(0)

directions = [
    [],  # 0
    ["r", "b", "l", "t"],  # 1
    ["lr", "tb"],  # 2
    ["tr", "rb", "bl", "lt"],  # 3
    ["ltr", "trb", "rbl", "blt"],  # 4
    ["tblr"],  # 5
]

def check(cur_r: int, cur_c: int, direction: str):
    positions = []
    count = 0
    for direct in direction:
        if direct == "l":
            for c in range(cur_c - 1, -1, -1):
                if office[cur_r][c] == 0:
                    positions.append((cur_r, c))
                    count += 1
                elif office[cur_r][c] == 6:
                    break
        elif direct == "t":
            for r in range(cur_r - 1, -1, -1):
                if office[r][cur_c] == 0:
                    positions.append((r, cur_c))
                    count += 1
                elif office[r][cur_c] == 6:
                    break
        elif direct == "r":
            for c in range(cur_c + 1, M):
                if office[cur_r][c] == 0:
                    positions.append((cur_r, c))
                    count += 1
                elif office[cur_r][c] == 6:
                    break
        elif direct == "b":
            for r in range(cur_r + 1, N):
                if office[r][cur_c] == 0:
                    positions.append((r, cur_c))
                    count += 1
                elif office[r][cur_c] == 6:
                    break
    return (positions, count)

def draw(positions, value):
    for _r, _c in positions:
        office[_r][_c] = value

min_blindspots = [sys.maxsize]  # 최소 사각지대

def DFS(n: int):
    if n == len(cctvs):
        cur_blindspots = calc_blindspots()
        if cur_blindspots == 0:
            print(0)
            exit(0)
        if min_blindspots[0] > cur_blindspots:
            min_blindspots[0] = cur_blindspots
        return

    type, r, c = cctvs[n]
    for direction in directions[type]:
        positions, _ = check(r, c, direction)
        draw(positions, "#")
        DFS(n + 1)
        draw(positions, 0)

DFS(0)
print(min_blindspots[0])