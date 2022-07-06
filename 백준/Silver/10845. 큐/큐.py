import sys 
from collections import deque

commands = []
for i in range(0, int(sys.stdin.readline().rstrip())):
    commands.append(sys.stdin.readline().rstrip())

queue = deque()
for command in commands:
    # pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    if command == "pop":
        print(queue.pop() if len(queue) != 0 else -1)
    # size: 큐에 들어있는 정수의 개수를 출력한다.
    elif command == "size":
        print(len(queue))
    # empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
    elif command == "empty":
        print(1 if len(queue) == 0 else 0)
    # front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif command == "front":
        print(queue[-1] if len(queue) != 0 else -1)
    # back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif command == "back":
        print(queue[0] if len(queue) != 0 else -1)
    # push X: 정수 X를 큐에 넣는 연산이다.
    elif command[0:4] == "push":
        queue.appendleft(int(command[5:]))
