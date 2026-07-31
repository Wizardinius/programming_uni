str1, str2, str3 = '123321', '123421', '123456'

def simmetry_check(str1ng):
    L = len(str1ng)
    am = 0
   #for i in range(L//2):
        #am += 1 if str1ng[i] == str1ng[L-1-i] else 0
    am = sum(1 for i in range(L//2) if str1ng[i] == str1ng[L-1-i])
    return am

print(f"str1 is {'YES' if simmetry_check(str1) in (3, 2) else 'NO'}")
print(f"str2 is {'YES' if simmetry_check(str2) in (3, 2) else 'NO'}")
print(f"str3 is {'YES' if simmetry_check(str3) in (3, 2) else 'NO'}")