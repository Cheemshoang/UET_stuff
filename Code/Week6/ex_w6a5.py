from typing import List
def check(arr: List, k: int) -> int:
    for i in range(arr):
        if arr[i] == k: return i
    
    return -1 