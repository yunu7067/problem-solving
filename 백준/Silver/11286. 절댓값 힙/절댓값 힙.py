from heapq import heappop, heappush
import sys
input = lambda: sys.stdin.readline().rstrip()
heap = []
for _ in range(int(input())):
    X = int(input())
    if X != 0:
        heappush(heap, (abs(X), X))
    else:
        print(heappop(heap)[1] if heap else "0")