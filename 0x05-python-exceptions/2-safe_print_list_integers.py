#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    count = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end='')
            i += 1
        except IndexError:
            raise IndexError
        except (ValueError, TypeError):
            i += 1
            continue
        else:
            count += 1
    print()
    return (count)
