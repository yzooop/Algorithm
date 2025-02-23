function solution(s) {
    const isLen = s.length === 4 || s.length === 6
    const isInt = [...s].filter((item) => !Number.isInteger(Number(item)))
    return isLen && isInt.length === 0
}