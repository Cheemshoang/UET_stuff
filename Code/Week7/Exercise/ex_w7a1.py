from typing import List, Tuple

ar = list(map(int, input().split()))
def check(arr: List[int])-> List[int]:
    seen = list()
    
    for i in arr:
        if i in seen:
            continue
        seen.append(i)
    return seen
print(check(ar))
