function solution(arr) {
    let x = 0;

    while (true) {
        const updatedArr = arr.map((item) =>
            item >= 50 && item % 2 === 0
                ? item / 2
                : item < 50 && item % 2 === 1
                ? item * 2 + 1
                : item
        );

        if (arr.every((value, index) => value === updatedArr[index])) {
            return x;
        }

        arr = updatedArr;
        x++;
    }
}
