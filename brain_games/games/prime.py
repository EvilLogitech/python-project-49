#!/usr/bin/env python3
import random


def get_number():
    return random.randint(1, 100)


def is_prime(num):
    res = []
    for i in range(1, num):
        if num % i == 0:
            res.append(i)
    if res == [1, num] or res == [1]:
        return 'yes'
    else:
        return 'no'


def make_game_step():
    num = get_number()
    correct_answer = is_prime(num)
    return (f'{str(num)}', str(correct_answer))


def get_rules():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    print(__name__)


if __name__ == '__main__':
    main()
