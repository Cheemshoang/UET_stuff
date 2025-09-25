n = str(input("Ten chu ho"))
a = int(input("Chi so thang truoc"))
b = int(input("Chi so thang nay"))

sum = 0
diff = b-a
price = [1984, 2050, 2380, 2998, 3350, 3460]

if diff <= 50:
    sum  = diff * price[0]
elif diff <= 100:
    sum = 50 * price[0] + (diff - 50) * price[1]
elif diff <= 200:
    sum = 50 * price[0] + 50 * price[1] + (diff - 100) * price[2]
elif diff <= 300:
    sum = 50 * price[0] + 50 * price[1] + 100 * price[2] + (diff - 200) * price[3]
elif diff <= 400:
    sum = 50 * price[0] + 50 * price[1] + 100 * price[2] + 100 * price[3] + (diff - 300) * price[4]
else:
    sum = (50 * price[0] + 50 * price[1] + 100 * price[2] + 
                 100 * price[3] + 100 * price[4] + (diff - 400) * price[5])
sum = int(sum*1.08)
print(f"Ho va ten {n}")
print(f"Tien phai tra: {sum}")

    
