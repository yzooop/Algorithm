import sys
input = sys.stdin.readline

N = int(input().strip())
org = N
count = 0 

while True:
    a = N // 10
    b = N % 10
    new = a + b
    N = b * 10 + new % 10
    count += 1

    if N == org:
        print(count)
        break