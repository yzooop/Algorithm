function solution(players, callings) {
    const rank = new Map();
    
    players.forEach((player, index) => {
        rank.set(player, index);
    });

    for (let call of callings) {
        let curIdx = rank.get(call);

        // 1등이면 넘어감
        if (curIdx > 0) {
            let prevIdx = curIdx - 1;
            let prevPlayer = players[prevIdx];

            // 바꾸고
            [players[curIdx], players[prevIdx]] = [players[prevIdx], players[curIdx]];

            // 저장
            rank.set(prevPlayer, curIdx);
            rank.set(call, prevIdx);
        }
    }
    return players;
}
