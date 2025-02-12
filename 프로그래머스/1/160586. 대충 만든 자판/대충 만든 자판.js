const keymap = ["ABACD", "BCEFD"]
const targets = ["ABCD","AABB"]

function solution(keymap, targets) {
    let keyDict = new Map()

    keymap.forEach((keys, keyIndex) => {
        [...keys].forEach((alp, alpIndex) => {
            if (keyDict.get(alp) === undefined || keyDict.get(alp) > alpIndex) {
                keyDict.set(alp, alpIndex + 1)
            }
        })
    })
    
    return targets.map((target) => {
        let answer = 0
        
        for (let t of target) {
            if (keyDict.get(t) === undefined) return -1
            answer += keyDict.get(t)
        }
        return answer
    })
}