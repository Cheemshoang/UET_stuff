from typing import List

a = list(map(int, input().split()))
x = int(input())
def delete(arr: List, x: int) -> List:
    
    return [i for i in arr if i >=x]
print(delete(a, x))