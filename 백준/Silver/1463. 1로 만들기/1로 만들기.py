import sys

X = int(sys.stdin.readline().rstrip())
D = [sys.maxsize] * (X + 1)
D[0], D[1] = 0, 0

for i in range(2, X + 1):
    counts = [D[i - 1] + 1]
    if i % 3 == 0:
        counts.append(D[i // 3] + 1)
    if i % 2 == 0:
        counts.append(D[i // 2] + 1)
    D[i] = min(counts)


print(D[X])