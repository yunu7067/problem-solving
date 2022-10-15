import sys

def op_priority(op: str):
    if op == "(":
        return 0
    elif op in "+-":
        return 1
    elif op in "*/":
        return 2
    else:
        return 3

def solution(exp):
    res, ops = [], []
    for op in exp:
        if op not in "()+-*/":
            res.append(op)
        elif op == "(":
            ops.append(op)
        elif op == ")":
            while ops and ops[-1] != "(":
                res += ops.pop()
            ops.pop()
        else:
            while ops and op_priority(op) <= op_priority(ops[-1]):
                res += ops.pop()
            ops.append(op)

    while ops:
        res += ops.pop()

    return "".join(res)

print(solution(sys.stdin.readline().rstrip()))