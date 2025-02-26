function solution(topping) {
    let leftSet = new Set();
    let rightMap = new Map();
    let count = 0;

    for (let t of topping) {
        rightMap.set(t, (rightMap.get(t) || 0) + 1);
    }

    for (let i = 0; i < topping.length - 1; i++) {
        leftSet.add(topping[i]);
        rightMap.set(topping[i], rightMap.get(topping[i]) - 1);

        if (rightMap.get(topping[i]) === 0) {
            rightMap.delete(topping[i]);
        }

        if (leftSet.size === rightMap.size) {
            count++;
        }
    }

    return count;
}
