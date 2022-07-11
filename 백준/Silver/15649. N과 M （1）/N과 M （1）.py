from re import A
import sys

N, M = map(int, sys.stdin.readline().split())
arr = [0] * M
is_used = [False] * N

def NM(k: int):
    if k == M:
        print(" ".join(map(str, arr)))
        return
    for num in range(0, N):
        if not is_used[num]:
            arr[k] = num + 1
            is_used[num] = True
            NM(k + 1)
            is_used[num] = False

NM(0)
