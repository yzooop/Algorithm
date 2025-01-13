function solution(str_list) {
    const idx_l = str_list.indexOf("l");
    const idx_r = str_list.indexOf("r");

    if (idx_l !== -1 && (idx_r === -1 || idx_l < idx_r)) {
        // "l"이 존재하고, "r"이 없거나 "l"이 "r"보다 먼저 나온 경우
        return str_list.slice(0, idx_l);
    } else if (idx_r !== -1 && (idx_l === -1 || idx_r < idx_l)) {
        // "r"이 존재하고, "l"이 없거나 "r"이 "l"보다 먼저 나온 경우
        return str_list.slice(idx_r + 1);
    } else {
        // "l"과 "r"이 모두 없는 경우
        return [];
    }
}
