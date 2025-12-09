arr = tuple(map(int, input().split()))
k = int(input())
n= len(arr)
k = k%n

arr_rearrange = arr[k:] + arr[:k]
print(arr_rearrange)