import sys
input = sys.stdin.readline

N = int(input())
node = {}
for _ in range(N):
    _v = input().split()
    node[_v[0]] = _v

travelsal = [[2, 1, 0], [2, 0, 1], [0, 2, 1]]

for orders in travelsal:
    stack, visited, res = ["A"], set([]), []
    while stack:
        cur = stack.pop()
        if (node[cur][1] == "." or node[cur][1] in visited) and (
            node[cur][2] == "." or node[cur][2] in visited
        ):
            res.append(cur)
            continue

        for order in orders:
            if node[cur][order] != ".":
                stack.append(node[cur][order])
                visited.add(node[cur][order])

    print(*res, sep="")