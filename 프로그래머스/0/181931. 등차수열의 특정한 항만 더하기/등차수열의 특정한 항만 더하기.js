function solution(a, d, included) {
    return included
            .map((item, idx) => item &&  d * idx + a)
            .filter((item) => item)
            .reduce((acc, cur) => acc + cur, 0)
}