import sys
input = sys.stdin.readline

second = [300, 60, 10]
result = []

T = int(input())

# 예외처리: T가 10의 배수가 아닌 경우
if T % 10 != 0:
    print(-1)
else:
    for i in second:
        result.append(T // i)
        T %= i
    print(" ".join(map(str, result)))
