import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input().strip())
arr = list(map(int, input().strip().split()))
p = list(permutations(arr, N))
answer = 0

for i in p:
    i_sum = 0
    
    for j in range(N-1):
        i_sum += abs(i[j] - i[j+1])
    answer = max(answer, i_sum)
print(answer)