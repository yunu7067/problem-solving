import sys

dr = [0, 0, 1, 1]
dc = [0, 1, 0, 1]

def Z(n, s, p):
    if n == 0:
        print(s)
        return
    next_n = n - 1
    next_half = pow(2, next_n)

    for i in range(4):
        next_r = dr[i] * next_half
        next_c = dc[i] * next_half

        if (dr[i] * next_half <= p[0] < next_half * (1 + dr[i])) and (
            dc[i] * next_half <= p[1] < next_half * (1 + dc[i])
        ):
            next_p = (p[0] - next_r, p[1] - next_c)
            next_s = s + next_half * next_half * (2 * dr[i] + 1 * dc[i])
            Z(next_n, next_s, next_p)


N, r, c = map(int, sys.stdin.readline().split())
Z(N, 0, (r, c))
