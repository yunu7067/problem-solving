from collections import defaultdict, deque
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
if M == 0:
    print(0)
    exit()
Edge = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    Edge[a].append(b)
    Edge[b].append(a)

q = deque([1])
inf = [False] * (N + 1)
inf[1] = True
count = 0
while q:
    cur = q.popleft()
    for next in Edge[cur]:
        if not inf[next]:
            q.append(next)
            inf[next] = True
            count += 1

print(count)