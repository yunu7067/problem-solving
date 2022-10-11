from collections import defaultdict, deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    V, E = map(int, input().split())
    vertex, visited = defaultdict(list), [0] * (V + 1)
    for _ in range(E):
        _s, _d = map(int, input().split())
        vertex[_s].append(_d)
        vertex[_d].append(_s)

    is_bipartite_Graph, g_idx = True, 1
    Q = deque()
    for v_idx in range(1, V + 1):
        if visited[v_idx] == 0:
            Q.append(v_idx)
            visited[v_idx] = g_idx
            g_idx += 1

        while Q and is_bipartite_Graph:
            cv = Q.popleft()
            for nv in vertex[cv]:
                if visited[nv] == 0:
                    Q.append(nv)
                    visited[nv] = -visited[cv]

                if visited[nv] != 0 and visited[nv] == visited[cv]:
                    is_bipartite_Graph = False
                    break

    print("YES" if is_bipartite_Graph else "NO")