import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    H, W, N = map(int, input().strip().split())

    # 층수 계산
    floor = N % H
    if floor == 0:
        floor = H

    # 호수 계산
    room = (N - 1) // H + 1

    # 결과 출력 (층수는 floor, 호수는 room으로 두 자리로 출력)
    print(f"{floor}{room:02}")
