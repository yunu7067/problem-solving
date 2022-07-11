import sys
input = lambda: sys.stdin.readline().split()

N, M = map(int, input())
nums = list(map(int, input()))
nums.sort()
arr = [-1] * M
is_used = [False] * N

def NM5(k: int):
    if k == M:
        print(" ".join(map(str, arr)))
        return
    for i, num in enumerate(nums):
        if not is_used[i]:
            is_used[i] = True
            arr[k] = num
            NM5(k + 1)
            is_used[i] = False

NM5(0)