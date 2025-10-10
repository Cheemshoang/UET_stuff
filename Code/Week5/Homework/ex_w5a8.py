def reverse_num(n):
    return int(str(n)[::-1])

def check_palindrome(n):
    return str(n) == str(n)[::-1]



def find_pal(n):
    cnt = 0
    cur = n
    
    while not check_palindrome(cur):
        re_num = reverse_num(cur)
        cur += re_num
        cnt += 1
        
    return cnt, cur

n = int(input())
step, num = find_pal(n)
print(f"step: {step}, num: {num}")