function solution(arr, n) {
    // 배열 길이에 따라 짝수 혹은 홀수 인덱스를 처리
    return arr.map((value, index) => {
        if (arr.length % 2 === 1) { // 길이가 홀수일 때
            return index % 2 === 0 ? value + n : value;
        } else { // 길이가 짝수일 때
            return index % 2 === 1 ? value + n : value;
        }
    });
}