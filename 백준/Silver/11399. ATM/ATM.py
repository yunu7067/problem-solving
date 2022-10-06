import sys

input = sys.stdin.readline
N = int(input())
people, wait = list(map(int, input().rstrip().split())), 0
people.sort()
for idx in range(N):
    wait += people[idx] * (N - idx)

print(wait)