import sys
input = sys.stdin.readline

A, B = map(int, input().strip().split())
C = int(input().strip())

if A + B < 2 * C:
    print(A+B)
else:
    print(A + B -  2 * C)