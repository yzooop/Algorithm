def solution(id_pw, db):
    input_id, input_pw = id_pw

    for user_id, user_pw in db:
        if user_id == input_id:
            if user_pw == input_pw:
                return "login"
            else:
                return "wrong pw"
    
    return "fail"
