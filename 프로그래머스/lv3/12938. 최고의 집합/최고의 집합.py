def solution(n, s):
    return (lambda div, mod: [(div if i < (n - mod) else div + 1) for i in range(n)])(*divmod(s, n)) if n <= s else [-1]
