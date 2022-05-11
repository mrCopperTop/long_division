# Long division

import random


def count_of_digits(number: int):
    """ Count the number of digits in a number """
    count = 0
    while number >= 1:
        number //= 10
        count += 1
    return count


def print_long_division(dividend: int, divisor: int):
    """ Print long division process """

    if divisor == 0:
        print('Error: division by zero')
        return

    if dividend < divisor:
        print('Dividend < divisor')
        return
    delimiter = ' | '
    print(f'{dividend}' + delimiter + f'{divisor}')
    quotient = dividend // divisor
    remainder = dividend % divisor

    is_first_step = True
    num_spaces = 0  # for sub_div line
    while dividend >= divisor:
        sub_div = dividend
        # dec_num = the number of decs to decrease dividend (it's also the number of the sub_div loop iterations)
        dec_num = 0
        while sub_div // divisor > 9:  # loop to find out sub_div
            sub_div = sub_div // 10
            dec_num += 1
        sub_quot = (sub_div // divisor) * divisor
        num_spaces_add = num_spaces + count_of_digits(sub_div) - count_of_digits(sub_quot)  # for sub_quot line
        if is_first_step == 1:
            print(' ' * num_spaces_add + f'{sub_quot}' +
                  ' ' * (len(f'{dividend}') - len(f'{sub_div}') + len(delimiter)) + f'{quotient}')
            is_first_step = False
        else:
            print(' ' * num_spaces + f'{sub_div}')
            print(' ' * num_spaces_add + f'{sub_quot}')

        sub_rem = sub_div - sub_quot
        if sub_rem == 0:
            num_spaces += count_of_digits(sub_div)
        else:
            num_spaces += count_of_digits(sub_div) - count_of_digits(sub_rem)

        dividend -= sub_quot * (10 ** dec_num)

    else:
        if remainder == 0:
            num_spaces -= 1
        print(' ' * num_spaces + f'{remainder}')


def main():
    dividend = random.randrange(1, 10**3, 1)
    divisor = random.randrange(1, 10**1, 1)
    # dividend = 8405
    # divisor = 6
    print_long_division(dividend, divisor)


if __name__ == '__main__':
    main()
