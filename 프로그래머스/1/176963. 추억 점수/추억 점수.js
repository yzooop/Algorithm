function solution(name, yearning, photo) {
    let scoreMap = new Map(name.map((n, i) => [n, yearning[i]]))
    
    return photo.map((p) => {
        const score = p.map(n => {
            return scoreMap.get(n) || 0
        })
        return score.reduce((acc, cur) => acc + cur, 0)
    })
}