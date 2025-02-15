function solution(n) {
    let num = n - 1; 
    
    for (let x = 2; x <= Math.sqrt(num); x++) {
        if (num % x === 0) {
            return x; 
        }
    }

    return num; 
}
