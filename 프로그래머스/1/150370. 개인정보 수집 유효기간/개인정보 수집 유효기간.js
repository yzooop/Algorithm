function solution(today, terms, privacies) {
    // today 날짜로 변환
    let [year, month, day] = today.split(".").map(Number)
    let date = new Date(year, month -1 , day)
  
    // terms map 만들기
    let termsMap = new Map()
    terms.forEach((t) => {
        let [type, month] = t.split(" ")
        month = Number(month)
        
        let expireDate = new Date(date)
        expireDate.setMonth(expireDate.getMonth() - month)
        termsMap.set(type, expireDate)
    })
    
    // 비교하고 처리
    return privacies
        .map((item, idx) => {
            let [exp, alp] = item.split(" ")
            const expDate = new Date(exp)
            return !(expDate > termsMap.get(alp)) ? idx + 1 : null
    }).filter((idx) => idx !== null)
}