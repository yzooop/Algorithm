import  sys

input = sys.stdin.readline

ans = []
for _ in range(10):
    n = int(input())
    x = n % 42
    ans.append(x)

print(len(set(ans)))