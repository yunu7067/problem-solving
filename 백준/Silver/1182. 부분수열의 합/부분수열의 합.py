import sys

N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

def find_sum(n: int, pos: int, sum: int):
    case = 0
    if n > 0 and sum == S:
        case += 1
    # 현재 위치가 마지막에 도달했으면
    if n == N or pos == N:
        return case
    for i in range(pos, N):
        case += find_sum(n + 1, i + 1, sum + nums[i])
    return case

print(find_sum(0, 0, 0))