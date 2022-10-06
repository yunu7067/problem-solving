import sys

input = sys.stdin.readline
N = int(input())
FULL, EMPTY = 0b1_11111_11111_11111_11111_1, 0b1_00000_00000_00000_00000_1
S = EMPTY
for _ in range(N):
    q = input().rstrip().split()
    inst = q[0]
    idx = int(q[1]) if len(q) == 2 else 0

    if inst == "add":
        S = S | (1 << idx)
    elif inst == "remove":
        S = S & (FULL - (1 << idx))
    elif inst == "check":
        print(bin(S)[23 - idx])
    elif inst == "toggle":
        S = S ^ (1 << idx)
    elif inst == "all":
        S = FULL
    elif inst == "empty":
        S = EMPTY