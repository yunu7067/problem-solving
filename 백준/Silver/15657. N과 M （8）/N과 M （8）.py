import sys
input = lambda: sys.stdin.readline().split()

N, M = map(int, input())
nums = list(map(int, input()))
nums.sort()
arr = [-1] * M

def NM8(k: int):
    if k == M:
        print(" ".join(map(str, arr)))
        return
    for num in nums:
        if arr[k - 1] <= num:
            arr[k] = num
            NM8(k + 1)
            arr[k] = -1

NM8(0)