import sys

N = int(sys.stdin.readline().strip())

lst = list(map(int, sys.stdin.readline().strip().split()))

v = int(sys.stdin.readline().strip())

cnt_v = lst.count(v)
print(cnt_v)