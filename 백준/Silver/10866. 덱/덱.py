import sys 
from collections import deque

commands = []
for i in range(0, int(sys.stdin.readline().rstrip())):
    commands.append(sys.stdin.readline().rstrip())

queue = deque()
for command in commands:
    # pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    if command == "pop_front":
        print(queue.pop() if len(queue) != 0 else -1)
    # pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif command == "pop_back":
        print(queue.popleft() if len(queue) != 0 else -1)
    # size: 덱에 들어있는 정수의 개수를 출력한다.
    elif command == "size":
        print(len(queue))
    # empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
    elif command == "empty":
        print(1 if len(queue) == 0 else 0)
    # front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif command == "front":
        print(queue[-1] if len(queue) != 0 else -1)
    # back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif command == "back":
        print(queue[0] if len(queue) != 0 else -1)
    # push_front X: 정수 X를 덱의 앞에 넣는다.
    elif command[0:10] == "push_front":
        queue.append(int(command[11:]))
    # push_back X: 정수 X를 덱의 뒤에 넣는다.
    elif command[0:9] == "push_back":
        queue.appendleft(int(command[10:]))