import sys
input = sys.stdin.readline

S = input().strip().lower()
alp = "abcdefghijklmnopqrstuvwxyz"
cnt = []

for al in alp:
    if al in S:
        cnt.append(S.count(al))
    else:
        cnt.append(0)

max_alp = max(cnt)
max_alp_idx = cnt.index(max_alp)

if cnt.count(max_alp) > 1:
    print("?")
else:
    print(alp[max_alp_idx].upper())