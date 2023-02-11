#!/usr/bin/env python3
import random

GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_round():
    """
    Prime game
    Player get a number and need to decide is it prime
    """
    res = []
    num = random.randint(1, 100)
    for i in range(1, num):
        if num % i == 0:
            res.append(i)
    correct_answer = 'yes' if res == [1, num] or res == [1] else 'no'
    return (f'{str(num)}', str(correct_answer))


def main():
    print(__name__)


if __name__ == '__main__':
    main()
