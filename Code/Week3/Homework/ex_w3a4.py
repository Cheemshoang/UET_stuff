c = str(input())
if (96 < ord(c[0]) < 123) or (64 < ord(c[0]) < 91): 
    print(f"{c} là kí tự alphabet")

else:
    print(f"{c} không phải là kí tự alphabet")
    
