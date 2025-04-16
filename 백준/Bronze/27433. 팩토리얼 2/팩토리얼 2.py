import sys
input = sys.stdin.readline

# func
def factorial(n):
  if n == 1 or n == 0:
    return 1
  
  return n * factorial(n-1)

# 입력
N = int(input().strip())

# 정답
print(factorial(N))