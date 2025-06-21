def solution(babbling):
    valid_sounds = ["aya", "ye", "woo", "ma"]
    count = 0

    for word in babbling:
        temp = word
        for sound in valid_sounds:
            if temp.count(sound) > 1:
                break
            temp = temp.replace(sound, ' ')
        if temp.strip() == '':
            count += 1

    return count
