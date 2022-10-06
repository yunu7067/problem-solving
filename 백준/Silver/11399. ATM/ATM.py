from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N = int(input())

people, wait = [], 0
for idx, time in enumerate(input().rstrip().split()):
    heappush(people, (int(time), idx))

while people:
    wait += heappop(people)[0] * N
    N -= 1

print(wait)