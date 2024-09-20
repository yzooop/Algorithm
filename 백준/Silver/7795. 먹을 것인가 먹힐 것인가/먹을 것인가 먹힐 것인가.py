import sys
from bisect import bisect_left

input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    A, B = map(int, input().strip().split())
    A_list = list(map(int, input().strip().split()))
    B_list = list(map(int, input().strip().split()))

    # B_list를 정렬
    B_list.sort()

    cnt = 0
    for a in A_list:
        # B_list에서 a보다 작은 값들의 개수를 이분 탐색으로 찾음
        cnt += bisect_left(B_list, a)

    print(cnt)
