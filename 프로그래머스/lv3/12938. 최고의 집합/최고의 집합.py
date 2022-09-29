def solution(n, s):
    if n > s:
        return [-1]
    (div, mod) = divmod(s, n)
    return [(div if i < (n - mod) else div + 1) for i in range(n)]
