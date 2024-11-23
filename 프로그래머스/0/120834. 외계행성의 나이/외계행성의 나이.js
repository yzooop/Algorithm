function solution(age) {
    const planet_age = "abcdefghij"
    
    return age
        .toString()
        .split("")
        .map((idx) => planet_age[idx])
        .join("")
}