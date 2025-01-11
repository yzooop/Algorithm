function solution(date1, date2) {
    const d1 = Date.UTC(date1[0], date1[1], date1[2])
    const d2 = Date.UTC(date2[0], date2[1], date2[2])
    return d1 < d2 ? 1 : 0
}