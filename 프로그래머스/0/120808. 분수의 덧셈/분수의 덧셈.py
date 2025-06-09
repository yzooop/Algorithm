import math

def solution(numer1, denom1, numer2, denom2):
    gcd_val = math.gcd(denom1, denom2)
    lcm = gcd_val * (denom1 // gcd_val) * (denom2 // gcd_val)
    x = (lcm // denom1) * numer1 + (lcm // denom2) * numer2

    common = math.gcd(x, lcm)
    return [x // common, lcm // common]
