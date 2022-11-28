def is_armstrong(n):
    str_number = str(n)
    if int(str_number[0])**3 + int(str_number[1])**3 + int(str_number[2])**3 == n:
        return True
    return False


print(is_armstrong(153)) 
print(is_armstrong(370)) 
print(is_armstrong(254)) 
print(is_armstrong(111))