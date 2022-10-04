from collections import defaultdict, deque
import sys

input = sys.stdin.readline

N = int(input())
node = defaultdict(list)
for _ in range(N - 1):
    _s, _e = map(int, input().rstrip().split())
    node[_s].append(_e)
    node[_e].append(_s)

parent_node = defaultdict(int)
parent_node[1] = 1
Q = deque([1])
while Q:
    cur_node = Q.popleft()
    for next_node in node[cur_node]:
        if parent_node[next_node] != 0:
            continue
        parent_node[next_node] = cur_node
        Q.append(next_node)

for i in range(2, N + 1):
    print(parent_node[i])