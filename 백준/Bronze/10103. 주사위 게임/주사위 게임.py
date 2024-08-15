import  sys
input = sys.stdin.readline

n = int(input().strip())

ans_a , ans_b = 100, 100

for _ in range(n):
    a, b = map(int, input().strip().split())

    if a < b:
        ans_a -= b
    elif a > b :
        ans_b -= a

print(ans_a)
print(ans_b)