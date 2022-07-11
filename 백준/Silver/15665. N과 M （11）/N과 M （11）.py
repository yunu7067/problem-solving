import sys
input = lambda: sys.stdin.readline().split()

N, M = map(int, input())
nums = list(set(map(int, input())))
nums.sort()
arr = [-1] * M

def NM11(k: int):
    if k == M:
        print(" ".join(map(str, arr)))
        return
    for i in range(0, len(nums)):
        arr[k] = nums[i]
        NM11(k + 1)

NM11(0)