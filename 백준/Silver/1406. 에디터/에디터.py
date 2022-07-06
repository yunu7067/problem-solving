from collections import deque
import sys

text = sys.stdin.readline().rstrip()
commands_count = int(sys.stdin.readline().rstrip())
commands = []
for i in range(0, commands_count):
    commands.append(sys.stdin.readline().rstrip())

left = deque(text)
right = deque()

for command in commands:
    # 커서 왼쪽 이동
    if command[0] == "L":
        if len(left) != 0:
            right.appendleft(left.pop())
    # 커서 오른쪽 이동
    elif command[0] == "D":
        if len(right) != 0:
            left.append(right.popleft())
    # 왼쪽 글자 삭제
    elif command[0] == "B":
        if len(left) != 0:
            left.pop()
    # 오른쪽에 글자 추가
    elif command[0] == "P":
        left.append(command[2])

print("".join(list(left) + list(right)))