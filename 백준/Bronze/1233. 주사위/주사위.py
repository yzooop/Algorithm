import sys
input = sys.stdin.readline

s1, s2, s3 = map(int, input().strip().split())

frequency = {}

for n_1 in range(1, s1 + 1):
    for n_2 in range(1, s2 + 1):
        for n_3 in range(1, s3 + 1):
            sum_value = n_1 + n_2 + n_3

            if sum_value in frequency:
                frequency[sum_value] += 1
            else:
                frequency[sum_value] = 1

max_frequency = max(frequency.values())
result = min([key for key, value in frequency.items() if value == max_frequency])

print(result)
