#!/usr/bin/env python3
import random


def get_number():
    return random.randint(0, 100)


def euclid_gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1 + num2


def make_game_step():
    num1, num2 = get_number(), get_number()
    correct_answer = str(euclid_gcd(num1, num2))
    return (f'{str(num1)} {str(num2)}', correct_answer)


def get_rules():
    return 'Find the greatest common divisor of given numbers.'


def main():
    print(__name__)


if __name__ == '__main__':
    main()
