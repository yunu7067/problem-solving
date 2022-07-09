import sys 
hh, mm = map(int, sys.stdin.readline().split())
if mm < 45:
    print(f"{hh-1 if hh > 0 else 23} {60+mm-45}")
else:
    print(f"{hh} {mm-45}")