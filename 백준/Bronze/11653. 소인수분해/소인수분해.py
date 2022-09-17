import sys

N = int(sys.stdin.readline().rstrip())
i = 2
while N > 1:
    div, mod = divmod(N, i)
    if mod == 0:
        N = div
        print(i)
    else:
        i += 1