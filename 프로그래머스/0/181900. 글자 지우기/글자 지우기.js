function solution(my_string, indices) {
    let arr = [...my_string]
    
    for (const i of indices) {
        arr[i] = ""
    }
    return arr.join("")
}