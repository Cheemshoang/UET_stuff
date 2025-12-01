from typing import List
def check(arr: List, k: int) -> int:
    for i in range(len(arr)):
        if arr[i] == k: return i + 1
    
    return -1 
print(check([2,3,4,5], 3))