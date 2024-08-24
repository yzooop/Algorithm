import sys
input = sys.stdin.readline

# 학점 : score
# 과목평점 : grade
# (학점 * 과목평점)의 합 / 학점총합

alp_list = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"] # 등급
grade_list = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0] # 과목평점

# 학점 모음
score_sum = 0

# 학점 * 과목평점 모음
total = 0

# 과목명, 학점, 등급 순
for _ in range(20):
    arr = list(map(str, input().strip().split()))
    arr[1] = float(arr[1])

    if arr[2] == "P": 
        continue

    if arr[2] in alp_list:
        i = alp_list.index(arr[2])
        grade = grade_list[i]
        total += arr[1] * grade
        score_sum += arr[1]

if score_sum == 0:
    print(f"{0.000000:.6f}")
else:
    gpa = total / score_sum
    print(f"{gpa:.6f}")