#!/usr/bin/env python3
import random


def get_number():
    return random.randint(0, 100)


def get_operator():
    operators = ['+', '-', '*']
    return random.choice(operators)


def make_game_step():
    num1, num2 = get_number(), get_number()
    op = get_operator()
    if op == '+':
        correct_answer = num1 + num2
    elif op == '-':
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2
    return (f'{num1} {op} {num2}', str(correct_answer))


def get_rules():
    return 'What is the result of the expression?'


def main():
    print(__name__)


if __name__ == '__main__':
    main()
