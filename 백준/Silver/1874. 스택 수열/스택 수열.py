from collections import deque

# from heapq import heappop, heappush
import sys

input = sys.stdin.readline
N = int(input())

stack, next = [0], 1
history = []
is_stackable = True

for _ in range(N):
    target = int(input())
    top = stack[len(stack) - 1]
    if top < target < next:
        is_stackable = False
        break
    if top < target:
        while top != target:
            history.append("+")
            stack.append(next)
            top = next
            next += 1
    elif top > target:
        while top != target:
            history.append("-")
            stack.pop()
            top = stack[len(stack) - 1]

    if top == target:
        history.append("-")
        stack.pop()
if is_stackable:
    print(*history, sep="\n")
else:
    print("NO")