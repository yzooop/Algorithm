function solution(str_list, ex) {
    let str = ""
    return str_list.map((item) => item.includes(ex) ? str : str + item).join("")
}