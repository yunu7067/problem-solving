from collections import deque
import sys
input = sys.stdin.readline

class Gear:
    def __init__(self, teeth, gear_index):
        self.teeth1 = deque(teeth[6:8] + teeth[0:2])
        self.teeth2 = deque(teeth[2:6])
        self.gear_index = gear_index

    def left_polar(self):
        return self.teeth1[0]

    def right_polar(self):
        return self.teeth2[0]

    def turn(self, direction):
        if direction == 1:
            self.teeth1.appendleft(self.teeth2.pop())
            self.teeth2.appendleft(self.teeth1.pop())
        else:
            self.teeth1.append(self.teeth2.popleft())
            self.teeth2.append(self.teeth1.popleft())

    def score(self):
        return self.teeth1[2] * (2**self.gear_index)

Gears = [Gear(list(map(int, input().rstrip())), _i) for _i in range(4)]

for _ in range(int(input())):
    cur_gear, turn_dir = map(int, input().split())
    cur_gear -= 1
    # 전체 기어 회전 계산
    fix_turn_dirs = [-1, 1, -1, 1]
    if fix_turn_dirs[cur_gear] != turn_dir:
        fix_turn_dirs = [1, -1, 1, -1]
    # 기어 회전 체크
    visited = [False, False, False, False]
    visited[cur_gear] = True
    for left in range(cur_gear - 1, -1, -1):
        if Gears[left].right_polar() == Gears[left + 1].left_polar():
            break
        visited[left] = True
    for right in range(cur_gear + 1, 4):
        if Gears[right].left_polar() == Gears[right - 1].right_polar():
            break
        visited[right] = True
    # 기어 회전
    for i in range(4):
        if visited[i]:
            Gears[i].turn(fix_turn_dirs[i])

print(sum(map(lambda x: x.score(), Gears)))