import sys
input = lambda: sys.stdin.readline().split()

N, M = map(int, input())
nums = list(map(int, input()))
nums.sort()
arr = [0] * M

def NM7(k: int):
    if k == M:
        print(" ".join(map(str, arr)))
        return
    for i in range(0, N):
        arr[k] = nums[i]
        NM7(k + 1)

NM7(0)
