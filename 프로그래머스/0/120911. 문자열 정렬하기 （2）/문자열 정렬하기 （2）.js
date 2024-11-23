function solution(my_string) {
    const arr = my_string.toLowerCase().split("")
    const sorted_arr = arr.sort()
    return sorted_arr.join("")
    
}