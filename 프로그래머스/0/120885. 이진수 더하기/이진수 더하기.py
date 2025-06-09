def solution(bin1, bin2):
    plus = (int(bin1, 2) + int(bin2, 2))
    return format(plus, 'b')