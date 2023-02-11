#!/usr/bin/env python3
import random

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_round():
    """
    Even game
    Player get a number and need to find is it even
    """
    num = random.randint(0, 100)
    correct_answer = 'yes' if num % 2 == 0 else 'no'
    return (str(num), correct_answer)


def main():
    print(__name__)


if __name__ == '__main__':
    main()
