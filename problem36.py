#! /usr/bin/env python


def double_base_palindromes():
    final_list = []
    for x in range(1, 1000001):
        string = str(x)
        if string == string[::-1]:
            pass
        else:
            continue
        base_two = bin(x)[2:]
        if base_two == base_two[::-1]:
            final_list.append(x)
    return final_list


if __name__ == '__main__':
    print sum(double_base_palindromes())