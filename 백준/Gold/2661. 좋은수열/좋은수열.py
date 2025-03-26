def is_good(seq):
    length = len(seq)
    for i in range(1, length // 2 + 1):
        if seq[-i:] == seq[-2*i:-i]:
            return False
    return True

def backtrack(seq, N):
    if len(seq) == N:
        print(seq)
        exit()
    
    for num in '123':
        new_seq = seq + num
        if is_good(new_seq):
            backtrack(new_seq, N)

N = int(input())
backtrack("", N)
