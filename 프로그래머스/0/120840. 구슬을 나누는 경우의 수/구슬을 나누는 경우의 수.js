function solution(balls, share) {
    if (balls < share) return 0;
    
    let a = 1, b = 1;

    for (let i = 1; i <= share; i++) {
        a *= balls - i + 1;
        b *= i;
    }
    
    return Math.round(a / b);
}
