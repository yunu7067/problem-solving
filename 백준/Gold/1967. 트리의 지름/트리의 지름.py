from collections import defaultdict
import sys
from typing import List
sys.setrecursionlimit(10**5)

input = sys.stdin.readline
vertex = defaultdict(list)
N = int(input())
for _ in range(N - 1):
    _node, _leaf, _weight = map(int, input().split())
    vertex[_node].append((_leaf, _weight))

def get_diameter(node: int):
    orphan_diamenter, contain_diamenter = 0, 0
    if vertex[node]:
        leafs: List[List[int]] = [get_diameter(leaf[0]) for leaf in vertex[node]]
        leaf_weights = [leaf[1] + vertex[node][idx][1] for idx, leaf in enumerate(leafs)]
        leaf_weights.sort(reverse=True)
        contain_diamenter = leaf_weights[0]
        orphan_diamenter = max(*list(map(lambda x: x[0], leafs)), sum(leaf_weights[:2]))

    return [orphan_diamenter, contain_diamenter]

print(max(get_diameter(1)))