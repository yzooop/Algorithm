function solution(number) {
    let cnt = 0
    for (let a = 0; a < number.length; a++){
        for (let b = a + 1 ; b < number.length; b++) {
            for (let c = b + 1; c < number.length; c++) {
                if (number[a] + number[b] + number[c] === 0) {
                    cnt += 1
                }
            }
        }
    }
    return cnt
}