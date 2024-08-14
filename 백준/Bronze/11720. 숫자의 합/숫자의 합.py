import  sys
input = sys.stdin.readline

N = int(input())

string = input().strip()
n_arr = [int(i) for i in string]

print(sum(n_arr))