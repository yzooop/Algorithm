function solution(phone_number) {
    const len = phone_number.length
    
    return [...phone_number].map((item, idx) => idx < len - 4 ? "*" : item).join("")
}