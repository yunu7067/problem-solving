# from collections import defaultdict, deque
from heapq import heappop, heappush
import sys
from typing import List

input = sys.stdin.readline
N = int(input())
board = [list(map(int, input().rstrip().split())) for _ in range(N)]
white_count, blue_count = 0, 0


def func(s: List[int], e: List[int]):
    global white_count, blue_count

    sidewidth = e[0] - s[0] + 1
    expect_cnt = sidewidth**2
    cnt = 0
    for _r in range(s[0], e[0] + 1):
        for _c in range(s[1], e[1] + 1):
            cnt += board[_r][_c]
    if cnt == 0:
        white_count += 1
        return
    elif cnt == expect_cnt:
        blue_count += 1
        return
    else:
        half = sidewidth >> 1
        # 왼쪽위
        func(s, [e[0] - half, e[1] - half])
        # 오른쪽위
        func([s[0], s[1] + half], [e[0] - half, e[1]])
        # 왼쪽아래
        func([s[0] + half, s[1]], [e[0], e[1] - half])
        # 오른쪽아래
        func([s[0] + half, s[1] + half], e)


func([0, 0], [N - 1, N - 1])

print(white_count)
print(blue_count)