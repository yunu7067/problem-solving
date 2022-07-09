import sys

n = int(sys.stdin.readline().rstrip())

print(pow(2, n) - 1)


def func(src: int, dest: int, a: int):
    if a == 1:
        print(f"{src} {dest}")
        return
    func(src, 6 - src - dest, a - 1)
    print(f"{src} {dest}")
    func(6 - src - dest, dest, a - 1)


func(1, 3, n)
