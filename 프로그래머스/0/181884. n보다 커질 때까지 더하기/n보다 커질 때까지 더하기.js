// function solution(numbers, n) {
//     let sum = 0;
//     for (const number of numbers) {
//         console.log("number : ", number)
//         sum += number
//         console.log("지금까지의 합 : ", sum)
//         if (n < sum) {
//             console.log("출력 : ", sum)
//         }
//     }
//     console.log("sum : ", sum)
// }

function solution(numbers, n) {
    let sum = 0;
    for (const number of numbers) {
        sum += number
        if (n < sum) {
            return sum
        }
    }
}