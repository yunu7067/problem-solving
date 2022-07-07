import sys

text = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()
if len(text) < len(bomb):
    print(text)
else:
    stack = []
    len_bomb = len(bomb)
    trigger = bomb[-1]

    for c in text:
        stack.append(c)
        if c == trigger:
            if "".join(stack[-len_bomb:]) == bomb:
                del stack[-len_bomb:]
    if stack:
        print("".join(stack))
    else:
        print("FRULA")
