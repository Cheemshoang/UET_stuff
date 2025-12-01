def hamming(a: int, b: int):
    res = a^b
    sum = 0
    while(res > 0):
        sum += res & 1
        res >> 1
        
    return sum