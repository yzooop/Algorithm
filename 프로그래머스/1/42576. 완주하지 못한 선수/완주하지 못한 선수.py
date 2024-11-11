def solution(participant, completion):
    hash_map = {}
    hash_sum = 0    
    
    for i in participant:
        hash_map[hash(i)] = i
        hash_sum += hash(i)
    
    for j in completion:
        hash_sum -= hash(j)

    return hash_map[hash_sum]
        
