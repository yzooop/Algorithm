import sys

data = []

for _ in range(3):
    number = int(sys.stdin.readline().strip())
    data.append(number)

arr = [i+1 for i in range(5)]

for num in data:
    if (num in arr):
        arr.remove(num)

sorted_arr = sorted(arr)

print(sorted_arr[0])
print(sorted_arr[1])