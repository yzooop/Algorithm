function solution(arr, intervals) {
    const arr_1 = arr.slice(intervals[0][0] , intervals[0][1] + 1)
    const arr_2 = arr.slice(intervals[1][0] , intervals[1][1] + 1)
    return [].concat(...arr_1).concat(...arr_2)
}