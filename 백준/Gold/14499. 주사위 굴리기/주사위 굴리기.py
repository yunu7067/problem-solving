from collections import deque
import sys
input = sys.stdin.readline

class Dice:
    def __init__(self):
        self.dice = [deque([0]), deque([0, 0, 0]), deque([0]), deque([0])]
    def getTop(self) -> int:
        return self.dice[1][1]
    def getBottom(self) -> int:
        return self.dice[3][0]
    def setBottom(self, value) -> int:
        self.dice[3].append(value)
        return self.dice[3].popleft()
    def rotate(self, direction) -> None:
        if direction == 1:  # 오른쪽
            self.dice[1].appendleft(self.dice[3].pop())
            self.dice[3].append(self.dice[1].pop())
        elif direction == 2:  # 왼쪽
            self.dice[1].append(self.dice[3].pop())
            self.dice[3].append(self.dice[1].popleft())
        elif direction == 3:  # 위쪽
            temp = self.dice[1].pop()
            self.dice[2].appendleft(self.dice[1].pop())
            self.dice[3].appendleft(self.dice[2].pop())
            self.dice[0].appendleft(self.dice[3].pop())
            self.dice[1].append(self.dice[0].pop())
            self.dice[1].append(temp)
        else:  # 아래쪽
            temp = self.dice[1].pop()
            self.dice[0].appendleft(self.dice[1].pop())
            self.dice[3].appendleft(self.dice[0].pop())
            self.dice[2].appendleft(self.dice[3].pop())
            self.dice[1].append(self.dice[2].pop())
            self.dice[1].append(temp)

R, C, dice_r, dice_c, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
dice = Dice()
d = [[], [0, 1], [0, -1], [-1, 0], [1, 0]]
for direction in map(int, input().split()):
    dr, dc = d[direction]
    nr, nc = dice_r + dr, dice_c + dc
    if not (0 <= nr < R and 0 <= nc < C):
        continue
    dice_r, dice_c = nr, nc
    dice.rotate(direction)
    if board[dice_r][dice_c] == 0:
        board[dice_r][dice_c] = dice.getBottom()
    else:
        dice.setBottom(board[dice_r][dice_c])
        board[dice_r][dice_c] = 0
    print(dice.getTop())