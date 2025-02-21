function solution(n, arr1, arr2) {
    let map = [];

    for (let i = 0; i < n; i++) {
        let binary = (arr1[i] | arr2[i]).toString(2).padStart(n, '0'); 
        let row = binary.replace(/1/g, '#').replace(/0/g, ' ');
        map.push(row);
    }

    return map;
}