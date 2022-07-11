import sys
input = lambda: sys.stdin.readline().split()

N, M = map(int, input())
nums = list(set(map(int, input())))
nums.sort()
arr = [-1] * M

def NM12(k: int):
    if k == M:
        print(" ".join(map(str, arr)))
        return
    for num in nums:
        if arr[k - 1] <= num:
            arr[k] = num
            NM12(k + 1)
            arr[k] = -1

NM12(0)
