import sys
input = sys.stdin.readline
S = input().rstrip()
sum, temp, mul = 0, "", 1
for s in S:
    if s == "+":
        sum += int(temp) * mul
        temp = ""
    elif s == "-":
        sum += int(temp) * mul
        mul = -1
        temp = ""
    else:
        temp += s
sum += int(temp) * mul
print(sum)