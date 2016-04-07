def is_luhn_valid(cc): #Parametro ejemplo 4896889802135

    num = map(int, str(cc))
    return sum(num[::-2] + [sum(divmod(d * 2, 10)) for d in num[-2::-2]]) % 10 == 0
    

def calculate_luhn(cc):
    num = map(int, str(cc))
    check_digit = 10 - sum(num[-2::-2] + [sum(divmod(d * 2, 10)) for d in num[::-2]]) % 10
    return 0 if check_digit == 10 else check_digit