import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    R, S = map(str, input().strip().split())
    R = int(R)

    for i in S:
        print(i*R, end="")
    print("")
