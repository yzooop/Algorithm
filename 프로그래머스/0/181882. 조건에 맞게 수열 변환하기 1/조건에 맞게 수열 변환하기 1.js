function solution(arr) {
    return arr.map(x => {
        if (x >= 50 && x % 2 === 0) {
            return x / 2; // 50 이상이고 짝수일 때 2로 나눔
        } else if (x < 50 && x % 2 === 1) {
            return x * 2; // 50 미만이고 홀수일 때 2를 곱함
        } else {
            return x; // 나머지 경우 그대로
        }
    });
}
