import sys

T = int(sys.stdin.readline().rstrip())
D = [None] * 12
D[1], D[2], D[3] = 1, 2, 4

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    for i in range(4, n + 1):
        if D[i] is not None:
            continue
        D[i] = D[i - 1] + D[i - 2] + D[i - 3]

    print(D[n])