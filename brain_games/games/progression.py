#!/usr/bin/env python3
import random


def get_progression():
    progression = []
    start = random.randint(0, 100)
    step = random.randint(1, 10)
    for i in range(10):
        progression.append(start + (i * step))
    return progression


def make_game_step():
    progression = get_progression()
    mask = random.randint(0, 9)
    correct_answer = progression[mask]
    progression[mask] = '..'
    pr_str = str(progression).replace(",", "").replace("'", "").strip("[]")
    return (f"""{pr_str}""", str(correct_answer))


def get_rules():
    return 'What number is missing in the progression?'


def main():
    print(__name__)


if __name__ == '__main__':
    main()
