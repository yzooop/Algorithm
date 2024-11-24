function solution(numbers) {
    const arr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    arr.forEach((item) => {
        let split = numbers.split(item)
        let join = split.join(arr.indexOf(item))
        numbers = join
    })
    return Number(numbers)
}