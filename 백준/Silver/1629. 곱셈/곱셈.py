import sys

A, B, C = map(int, sys.stdin.readline().split())

r = 1
while B != 0:
    if B & 1:
        r = (r * A) % C
    A = (A * A) % C
    B >>= 1

print(r)