a = list(map(str, input().split()))

def push_zero_front(a):
    zeros = []
    nonzeros = []
    for x in a:
        if x == 0:
            zeros.append(x)
        else:
            nonzeros.append(x)
    return zeros + nonzeros

def push_zero_end(a):
    zeros = []
    nonzeros = []
    for x in a:
        if x == 0:
            zeros.append(x)
        else:
            nonzeros.append(x)
    return nonzeros + zeros
