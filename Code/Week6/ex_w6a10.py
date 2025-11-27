def check(a: str, b: str) -> bool:
    map = {}
    rev_map = {}
    
    for ca, cb in zip(a,b):
        if ca in map:
            if map[ca] != cb: return False
        else:
            map[ca] = cb
        
        if cb in rev_map:
            if rev_map[cb] != ca: return False
        else:
            rev_map[cb] = ca
    