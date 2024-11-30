function solution(numlist, n) {
    return (numlist
                .map((num) => [num, Math.abs(num - n)])
                .sort((a, b) => a[1] === b[1] ? b[0] - a[0] : [a[1] - b[1]])
                .map((item) => item[0])
               )
}