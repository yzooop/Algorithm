function gcd(a, b) {
    while (b !== 0) {
        let temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

function solution(n) {
    const gcdValue = gcd(n, 6);  // n과 6의 최대공약수 구하기
    const lcmValue = (n * 6) / gcdValue;  // 최소공배수 구하기
    return (lcmValue / 6);
}
