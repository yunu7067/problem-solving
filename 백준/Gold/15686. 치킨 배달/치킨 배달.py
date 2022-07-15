from itertools import combinations
import sys
from typing import List, Tuple

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
stores = []  # 치킨집
houses = []  # 가정집

for _r in range(N):
    for _c in range(N):
        if board[_r][_c] == 1:
            houses.append((_r, _c))
        elif board[_r][_c] == 2:
            stores.append((_r, _c))

store_combs = combinations(stores, M)

# 두 위치의 거리
def distance(a: Tuple, b: Tuple):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# 한 가정집과 여러 치킨집 중에서 최소거리
def min_distance(house: Tuple, stores: List):
    _min_dist = sys.maxsize
    for store in stores:
        _cur_dist = distance(house, store)
        if _min_dist > _cur_dist:
            _min_dist = _cur_dist
    return _min_dist

def func():
    min_sum = sys.maxsize
    for store_comb in store_combs:
        sum_cur_distance = 0
        for house in houses:
            sum_cur_distance += min_distance(house, list(store_comb))
        if sum_cur_distance < min_sum:
            min_sum = sum_cur_distance
    return min_sum

print(func())