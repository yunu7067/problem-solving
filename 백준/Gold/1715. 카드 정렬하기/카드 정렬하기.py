from heapq import heapify, heappop, heappush
import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
if N == 1:
    print(0)
    exit()

cards = [int(input()) for _ in range(N)]
heapify(cards)
s = 0
while len(cards) > 1:
    c_sum = heappop(cards) + heappop(cards)
    s += c_sum
    heappush(cards, c_sum)

print(s)