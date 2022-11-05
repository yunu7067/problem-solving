from heapq import heappush, heappop
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
gems, bags = [], []
for _ in range(N):
    heappush(gems, list(map(int, input().split())))
for _ in range(K):
    heappush(bags, int(input()))

total, gems_sorted_by_value = 0, []
for _ in range(K):
    cur_bag = heappop(bags)
    while gems and gems[0][0] <= cur_bag:
        gem = heappop(gems)
        # 가치가 큰 순으로 저장 (-가치, 무게)
        heappush(gems_sorted_by_value, (-gem[1], gem[0]))
    if gems_sorted_by_value:
        most_expensive_gem = heappop(gems_sorted_by_value)
        total += -most_expensive_gem[0]

print(total)