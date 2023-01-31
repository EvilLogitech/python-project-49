#!/usr/bin/env python3
import random


def get_number():
    return random.randint(0, 100)


def is_even(num):
    return True if num % 2 == 0 else False


def make_game_step():
    num = get_number()
    correct_answer = 'yes' if is_even(num) else 'no'
    return (str(num), correct_answer)


def get_rules():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    print(__name__)


if __name__ == '__main__':
    main()
