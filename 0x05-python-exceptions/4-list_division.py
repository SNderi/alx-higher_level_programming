#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    div_list = []
    while i < list_length:
        try:
            div = my_list_1[i] / my_list_2[i]
            i += 1
        except TypeError:
            print("wrong type")
            div = 0
            i += 1
        except ZeroDivisionError:
            print("division by 0")
            div = 0
            i += 1
        except IndexError:
            print("out of range")
            div = 0
            break
        finally:
            div_list.append(div)
    return (div_list)
