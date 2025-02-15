function solution(s) {
    const arr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    
    arr.forEach((word, index) => {
        s = s.split(word).join(index);
    });

    return Number(s);
}