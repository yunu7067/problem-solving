import sys


def balance(text):
    stack = []

    for char in text:
        if char == "(" or char == "[":
            stack.append(char)
        elif char == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                print("no")
                return
        elif char == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                print("no")
                return
    if len(stack) == 0:
        print("yes")
    else:
        print("no")


text = ""

while True:
    text = sys.stdin.readline().rstrip()
    # "."인 경우 종료
    if text == ".":
        break
    else:
        balance(text)
