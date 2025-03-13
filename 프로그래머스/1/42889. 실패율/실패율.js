function solution(N, stages) {
    let stageFailRates = [];
    let players = stages.length;
    
    for (let i = 1; i <= N; i++) {
        let count = stages.filter(stage => stage === i).length;
        let failRate = count / players;
        players -= count;
        
        stageFailRates.push({ stage: i, failRate: failRate || 0 });
    }
    
    return stageFailRates
        .sort((a, b) => b.failRate - a.failRate || a.stage - b.stage)
        .map(item => item.stage);
}