import sys
input = sys.stdin.readline

N = int(input())

player =[]
result = []

for _ in range(N):
    name = input().strip()
    player.append(name[0])

first_name = set(player)

for i in first_name:
    if player.count(i) >= 5:
        result.append(i)

result.sort()

if len(result) > 0 :
    print("".join(result))
else:
    print("PREDAJA")