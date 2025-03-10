function solution(my_string, m, c) {
    return [...my_string].map((item, idx) => idx % m === c - 1 ? item : "").join("")
}