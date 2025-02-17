function solution(price, money, count) {
    const fee = (1 + count) * price * count * 0.5
    
    if (fee > money) {
        return fee - money
    } else {
        return 0
    }
}