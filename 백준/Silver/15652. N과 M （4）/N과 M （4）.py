import sys

N, M = map(int, sys.stdin.readline().split())
arr = [-1] * M
is_used = [False] * N

def NM3(k: int):
    if k == M:
        print(" ".join(map(str, arr)))
        return
    for num in range(max(1, arr[k - 1]), N + 1):
        arr[k] = num
        NM3(k + 1)
        arr[k] = 0

NM3(0)
