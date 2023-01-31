#!/usr/bin/env python3
from brain_games.scripts.game_carcass import start_game
import brain_games.scripts.brain_calc as calc


def play_game():
    start_game(calc.get_rules, calc.make_game_step)


def main():
    print(__name__)


if __name__ == '__main__':
    main()
