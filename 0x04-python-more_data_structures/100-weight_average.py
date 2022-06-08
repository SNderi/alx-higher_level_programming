#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total = 0
    den = 0
    for i in my_list:
        total += i[0] * i[1]
        den += i[1]
    return float(total / den)
