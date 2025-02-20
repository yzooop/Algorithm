function solution(dartResult) {
    let scores = [];
    let currentScore = 0;

    for (let i = 0; i < dartResult.length; i++) {
        let char = dartResult[i];

        if (!isNaN(char)) {
            if (char === '1' && dartResult[i + 1] === '0') {
                currentScore = 10;
                i++;
            } else {
                currentScore = Number(char);
            }
        }
        
        // 점수
        else if (char === 'S') {
            scores.push(currentScore ** 1);
        } else if (char === 'D') {
            scores.push(currentScore ** 2);
        } else if (char === 'T') {
            scores.push(currentScore ** 3);
        }
        
        // 옵션
        else if (char === '*') {
            let len = scores.length;
            scores[len - 1] *= 2;
            if (len > 1) scores[len - 2] *= 2;
        } else if (char === '#') {
            scores[scores.length - 1] *= -1;
        }
    }

    return scores.reduce((sum, score) => sum + score, 0);
}
