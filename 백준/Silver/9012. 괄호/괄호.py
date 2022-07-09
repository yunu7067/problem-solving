import sys
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    text = sys.stdin.readline().rstrip()
    stack = []
    for c in text:
        if c == "(":
            stack.append(c)
        elif c == ")" and stack and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(c)
    if stack:
        print("NO")
    else:
        print("YES")
