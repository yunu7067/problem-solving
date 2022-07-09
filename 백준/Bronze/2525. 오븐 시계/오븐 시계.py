import sys
hh, mm = map(int, sys.stdin.readline().split())
time = int(sys.stdin.readline().rstrip())
(hh_add, mm_add) = divmod(mm + time, 60)
print(f"{hh + hh_add if hh + hh_add < 24 else hh+hh_add - 24} {mm_add}")
