function solution(lottos, win_nums) {
    // 1등 - 6개 다 / 2등 - 5개 / 3등 - 4개 / 4등 - 3개 / 5등 - 2개 / 낙첨 - 그 외
    
    // 0 개수
    const zero_cnt = lottos.filter(l => l === 0).length
    
    // 맞은 개수
    let correct = win_nums.filter((item) => lottos.includes(item)).length
    if (correct === 0) {
        correct = 1
    }
    
    // 최대로 맞을 수 있는 수
    let max = correct + zero_cnt
    if (max === 7) {
        max = 6
    }
    
    return [7 - max, 7 - correct]
    
}