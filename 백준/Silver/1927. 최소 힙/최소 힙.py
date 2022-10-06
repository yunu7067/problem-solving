from heapq import heappop, heappush
import sys

input = sys.stdin.readline
N = int(input())
heap = []

for _ in range(N):
    inst = int(input())
    if inst != 0:
        heappush(heap, inst)
    else:
        print(heappop(heap) if heap else 0)
