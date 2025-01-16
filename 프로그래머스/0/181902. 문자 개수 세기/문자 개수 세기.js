function solution(my_string) {
    const result = Array(52).fill(0); // 대문자(26) + 소문자(26) 배열 초기화
    const A_CHAR_CODE = 'A'.charCodeAt(0); // 'A'의 유니코드 값 (65)
    const a_CHAR_CODE = 'a'.charCodeAt(0); // 'a'의 유니코드 값 (97)

    for (const char of my_string) {
        const charCode = char.charCodeAt(0);
        if (char >= 'A' && char <= 'Z') {
            // 대문자
            result[charCode - A_CHAR_CODE]++;
        } else if (char >= 'a' && char <= 'z') {
            // 소문자
            result[26 + (charCode - a_CHAR_CODE)]++;
        }
    }

    return result;
}