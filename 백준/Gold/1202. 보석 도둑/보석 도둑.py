from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
gems = []
for _ in range(N):
    heappush(gems, list(map(int, input().split())))
bags = [int(input()) for _ in range(K)]
bags.sort()

total, gems_sorted_by_value = 0, []
for bag in bags:
    while gems and gems[0][0] <= bag:
        # 가치가 큰 순으로 저장 (-가치, 무게)
        heappush(gems_sorted_by_value, -heappop(gems)[1])
    if gems_sorted_by_value:
        total += -heappop(gems_sorted_by_value)

print(total)