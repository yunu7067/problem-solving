from collections import defaultdict, deque
import sys

input = sys.stdin.readline

N = int(input())
src, dest = map(int, input().rstrip().split())
M = int(input())
V, Visited = [[] for _ in range(N + 1)], [-1] * (N + 1)
Visited[src] = 0

for _ in range(M):
    _s, _d = map(int, input().rstrip().split())
    V[_s].append(_d)
    V[_d].append(_s)

Q = deque([src])
while Q:
    cur = Q.popleft()
    for next in V[cur]:
        if Visited[next] == -1:
            Visited[next] = Visited[cur] + 1
            Q.append(next)

print(Visited[dest])