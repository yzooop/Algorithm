import sys
input = sys.stdin.readline

cnt = 0
while True:
    L, P, V = map(int, input().strip().split())

    if (L == 0 and P == 0 and V == 0):
        break

    num = ((V // P) * L) + min((V % P), L)
    cnt += 1

    print(f"Case {cnt}: {num}")