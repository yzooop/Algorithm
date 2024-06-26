import sys

# 총금액
X = int(sys.stdin.readline().strip())

# 구매 물건의 종류 수
N = int(sys.stdin.readline().strip())

price = []
quantity = []
sum = 0

for _ in range(N):
    a, b = map(int, sys.stdin.readline().strip().split())
    price.append(a)
    quantity.append(b)

for i in range(N):
    sum += price[i] * quantity[i]

if(sum == X):
    print("Yes")
else:
    print("No")

