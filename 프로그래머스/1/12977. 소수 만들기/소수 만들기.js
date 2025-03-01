function solution(nums) {
    let cnt = 0
    
    for (let a = 0; a < nums.length - 2; a++) {
        for (let b = a + 1; b < nums.length - 1; b++) {
            for (let c = b + 1; c < nums.length ; c++) {
                if (is_prime(nums[a] + nums[b] + nums[c])) {
                    cnt++
                }
            }
        }
    }
    return cnt
}

function is_prime(n) {
    let cnt = 0
    for(let i = 1; i <= n; i++) {
        if (n % i === 0){
            cnt++
        }
    }
    return cnt === 2 ? true : false
}