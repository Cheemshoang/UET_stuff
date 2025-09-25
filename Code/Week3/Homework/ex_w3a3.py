c = str(input())
if 96 < ord(c[0]) < 123: 
    print(chr(ord(c[0])-32))

else:
    print(chr(ord(c[0])+32))
    
