import sys

N = int(sys.stdin.readline().strip())

digit_10 = N // 10 # 2
digit_1 = N % 10 # 6
plus = digit_10 + digit_1 # 8
new = digit_1 * 10 + plus # 14
digit_1 = new % 10 # 4
new = plus * 10 + digit_1 # 84




print(digit_10)
print(digit_1)