#!/usr/bin/env python3
import random

GAME_RULES = 'What number is missing in the progression?'


def game_round():
    """
    Progression game
    Player get number progression and need to find missed number
    """
    progression = []
    start = random.randint(0, 100)
    step = random.randint(1, 10)
    for i in range(10):
        progression.append(start + (i * step))
    mask = random.randint(0, 9)
    correct_answer, progression[mask] = progression[mask], '..'
    prog_str = str(progression).replace(",", "").replace("'", "").strip("[]")
    return (prog_str, str(correct_answer))


def main():
    print(__name__)


if __name__ == '__main__':
    main()
