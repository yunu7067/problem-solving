import sys

input = sys.stdin.readline
N = int(input())
edge = [[] for _ in range(N + 1)]
diameter = [[0, 0] for _ in range(N + 1)]
for _ in range(N - 1):
    _node, _leaf, _weight = map(int, input().split())
    edge[_node].append(_leaf)
    diameter[_leaf][1] = _weight

def calc_diameter():
    S, visited = [1], [False for _ in range(N + 1)]

    while S:
        cur_node = S[-1]
        if not visited[cur_node] and edge[cur_node]:
            visited[cur_node] = True
            S.extend(edge[cur_node])
            continue
        S.pop()
        visited[cur_node] = True
        leafs = [diameter[leaf] for leaf in edge[cur_node]]
        leaf_weights = [leaf[1] for leaf in leafs]
        leaf_weights.sort(reverse=True)
        diameter[cur_node][0] = max([sum(leaf_weights[:2]), *list(map(lambda x: x[0], leafs))])
        diameter[cur_node][1] += leaf_weights[0] if leaf_weights else 0

calc_diameter()
print(max(diameter[1]))