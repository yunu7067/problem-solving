import sys

def Fibonacci(n: int, pp: int, p: int):
    if n <= 0:
        return pp + p
    return Fibonacci(n - 1, p, pp + p)


N = int(sys.stdin.readline().rstrip())
print(Fibonacci(N - 2, 0, 1) if N != 0 else 0)