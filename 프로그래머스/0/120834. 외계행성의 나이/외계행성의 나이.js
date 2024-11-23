function solution(age) {
    const planet_age = "abcdefghij"
    const age_str = age.toString()
    let ans = []
    
    for (let i = 0; i < age_str.length; i++){
        for (let j = 0; j < planet_age.length; j++){
            if (age_str[i] == j){
                ans.push(planet_age[j])
            }
        }
    }
    return ans.join("")
    
}