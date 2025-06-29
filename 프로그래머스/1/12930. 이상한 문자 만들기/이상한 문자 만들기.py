def solution(s):
    words = s.split(" ")
    
    ans = []
    for word in words:
        flip = ''
        for i in range(len(word)):
            if i % 2 == 0:
                flip += word[i].upper()
            
            else:
                flip += word[i].lower()
        ans.append(flip)
    
    return(" ".join(ans))

    