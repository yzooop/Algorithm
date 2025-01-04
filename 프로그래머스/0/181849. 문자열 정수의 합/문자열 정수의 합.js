function solution(num_str) {
    return [...num_str].map((item) => Number(item)).reduce((cur, acc) => cur + acc)
}