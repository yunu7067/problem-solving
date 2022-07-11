import sys
input = lambda: sys.stdin.readline().split()

N, M = map(int, input())
nums = list(map(int, input()))
nums.sort()
arr = [-1] * M
is_used = [False] * N

def NM9(k: int):
    if k == M:
        print(" ".join(map(str, arr)))
        return
    for i in range(0, N):
        if not is_used[i] and arr[k] != nums[i]:
            is_used[i] = True
            arr[k] = nums[i]
            NM9(k + 1)
            is_used[i] = False
    arr[k] = -1

NM9(0)