import sys
input = sys.stdin.readline

en = [500, 100, 50, 10, 5, 1]

price = int(input())
money = 1000 - price

cnt = 0

for i in en:
    cnt += money // i
    money %= i

print(cnt)