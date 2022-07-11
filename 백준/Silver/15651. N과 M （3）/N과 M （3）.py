import sys

N, M = map(int, sys.stdin.readline().split())
arr = [0] * M

def NM3(k: int):
    if k == M:
        print(" ".join(map(str, arr)))
        return
    for num in range(0, N):
        arr[k] = num + 1
        NM3(k + 1)
        arr[k] = 0

NM3(0)