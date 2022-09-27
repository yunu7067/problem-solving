from collections import defaultdict
import sys

input = sys.stdin.readline
D = [None] * 41
D[0], D[1] = [0, [1, 0]], [1, [0, 1]]

def fibonacci(n: int):
    global D

    if n == 0:
        return D[0]
    elif n == 1:
        return D[1]
    else:
        a = fibonacci(n - 1) if not D[n - 1] else D[n - 1]
        b = fibonacci(n - 2) if not D[n - 2] else D[n - 2]
        D[n] = [a[0] + b[0], [a[1][0] + b[1][0], a[1][1] + b[1][1]]]
        return D[n]

for _ in range(int(input())):
    num = int(input())
    if not D[num]:
        fibonacci(num)
    print(*D[num][1])