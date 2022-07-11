import sys
input = lambda: sys.stdin.readline().split()

N, M = map(int, input())
nums = list(map(int, input()))
nums.sort()
arr = [-1] * M

def NM6(k: int):
    if k == M:
        print(" ".join(map(str, arr)))
        return
    for i in range(0, N):
        if k >= 0 and nums[i] > arr[k - 1]:
            arr[k] = nums[i]
            NM6(k + 1)
            arr[k] = -1

NM6(0)