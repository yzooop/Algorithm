function solution(n) {
    const arr = Array.from({length: 300}, (_, i) => i + 1)
    const filterd_arr = arr
                        .filter((item) => !item.toString().includes("3"))
                        .filter((item) => item % 3 !== 0)
    return filterd_arr[n-1]
}