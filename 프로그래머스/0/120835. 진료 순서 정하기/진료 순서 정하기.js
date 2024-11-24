function solution(emergency) {
    const sorted = emergency.slice().sort((a, b) => b - a)
    // emergency.forEach((item) => {
    //     arr.push(sorted.indexOf(item) + 1)
    // })
    return emergency.map((item) => sorted.indexOf(item) + 1)
}