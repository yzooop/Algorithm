function solution(name, yearning, photo) {
    let scoreMap = new Map()
    
    for (let i=0; i < name.length; i++){
        scoreMap.set(name[i], yearning[i])
    }
    
    return photo.map((p) => {
        const score = p.map(n => {
            return scoreMap.get(n) ? scoreMap.get(n) : 0
        })
        return score.reduce((acc, cur) => acc + cur, 0)
    })
}