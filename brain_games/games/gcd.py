#!/usr/bin/env python3
import random


def get_number():
    return random.randint(0, 100)


def get_gcd(num):
    gcd = []
    for i in range(1, num // 2):
        if num % i == 0:
            gcd.append(i)
    gcd.append(num)
    return gcd


def make_game_step():
    num1, num2 = get_number(), get_number()
    gcd1, gcd2 = get_gcd(num1), get_gcd(num2)
    gcd1.reverse()
    gcd2.reverse()
    gcd_both = []
    for i in gcd1:
        if i in gcd2:
            gcd_both.append(i)
    correct_answer = str(gcd_both[0])
    return (f'{str(num1)} {str(num2)}', correct_answer)


def get_rules():
    return 'Find the greatest common divisor of given numbers.'


def main():
    print(__name__)


if __name__ == '__main__':
    main()
