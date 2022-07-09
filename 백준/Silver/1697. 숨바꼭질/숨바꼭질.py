import sys
from collections import deque

A, B = map(int, sys.stdin.readline().split())
Q = deque([A])
board = [sys.maxsize] * (max(A, B) * 2 + 1)
board[A], board[B] = 0, 0
cases = [lambda x: x + 1, lambda x: x - 1, lambda x: x * 2]

if A == B:
    print(0)
    exit(0)

while Q:
    cur_pos = Q.popleft()
    for case in cases:
        next_pos = case(cur_pos)
        if next_pos == B:
            print(board[cur_pos] + 1)
            exit(0)
        if 0 <= next_pos < len(board) and board[next_pos] == sys.maxsize:
            Q.append(next_pos)
            board[next_pos] = board[cur_pos] + 1