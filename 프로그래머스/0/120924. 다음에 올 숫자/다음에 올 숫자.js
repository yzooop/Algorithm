function solution(common) {
    // 등차수열인지 등비수열인지 확인
    const diff = common[1] - common[0]; // 첫 번째 공차
    const ratio = common[1] / common[0]; // 첫 번째 공비

    // 등차수열인지 확인
    if (common[2] - common[1] === diff) {
        return common[common.length - 1] + diff;
    }

    // 등비수열인 경우
    return common[common.length - 1] * ratio;
}