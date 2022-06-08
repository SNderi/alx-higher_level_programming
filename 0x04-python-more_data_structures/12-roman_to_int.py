#!/usr/bin/python3
def roman_to_int(roman_string):
    symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) == NoneType or type(roman_string) != str:
        return (0)
    res = 0
    i = 0
    while (i < len(roman_string)):
        num1 = symbols[roman_string[i]]
        if (i + 1 < len(roman_string)):
            num2 = symbols[roman_string[i + 1]]
            if (num1 >= num2):
                res = res + num1
                i = i + 1
            else:
                res = res + num2 - num1
                i = i + 2
        else:
            res = res + num1
            i = i + 1
    return res
