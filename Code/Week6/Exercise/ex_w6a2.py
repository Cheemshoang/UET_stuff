from typing import List, Tuple
def swap(a,b) -> Tuple[int, int]:
    return b,a

a,b = list(map(int, input().split()))
print(swap(a,b))