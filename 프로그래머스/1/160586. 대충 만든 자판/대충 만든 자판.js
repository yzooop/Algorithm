function solution(keymap, targets) {
    let keyDict = {};
    
    keymap.forEach((keys, keyIndex) => {
        [...keys].forEach((char, pressIndex) => {
            if (keyDict[char] === undefined || keyDict[char] > pressIndex + 1) {
                keyDict[char] = pressIndex + 1;
            }
        });
    });

    return targets.map(target => {
        let pressCount = 0;
        for (let char of target) {
            if (keyDict[char] === undefined) return -1;
            pressCount += keyDict[char];
        }
        return pressCount;
    });
}
