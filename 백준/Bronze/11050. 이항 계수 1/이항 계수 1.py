from math import factorial
import sys

N, M = map(int, sys.stdin.readline().split())
print(int(factorial(N) / (factorial(N - M) * factorial(M))))