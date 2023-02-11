#!/usr/bin/env python3
import random

GAME_RULES = 'Find the greatest common divisor of given numbers.'


def euclid_gcd(num1, num2):
    """Euclid algorithm to calculate gcd"""
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1 + num2


def game_round():
    """
    GCD game
    Player get two numbers and need to find greatest common divisor
    """
    num1, num2 = random.randint(0, 100), random.randint(0, 100)
    correct_answer = str(euclid_gcd(num1, num2))
    return (f'{str(num1)} {str(num2)}', correct_answer)


def main():
    print(__name__)


if __name__ == '__main__':
    main()
