function solution(s){
    const p_cnt = [...s].filter((item) => item === 'p' || item === 'P').length
    const y_cnt = [...s].filter((item) => item === 'y' || item === 'Y').length
    return p_cnt === y_cnt
}