function solution(code) {
    let ret = "";
    let mode = 0;

    for (let i = 0; i < code.length; i++) {
        if (code[i] === "1") {
            mode = 1 - mode; // mode 변경 (0 ↔ 1)
        } else if ((mode === 0 && i % 2 === 0) || (mode === 1 && i % 2 === 1)) {
            ret += code[i]; // 조건을 만족하면 ret에 추가
        }
    }

    return ret === "" ? "EMPTY" : ret;
}