n = int(input())
arr = list(map(int, input().split()))
found = False
for i in range(n):
    
    if arr[i] == 42:
        found = True
        break
    
if found: 
    print("I've found the meaning of life!")
else:
    print("Its a joke")